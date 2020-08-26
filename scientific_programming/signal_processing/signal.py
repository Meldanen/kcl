import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import signal
from scipy.stats import pearsonr
from dtw import dtw
from enum import Enum

matplotlib.use('TkAgg')


# Enum for the sampling type used for re-discretising signals
class ResamplingType(Enum):
    UP_SAMPLE = 1
    DOWN_SAMPLE = 2


# Enum containing the different signal types and their maximum values
class SignalType(Enum):
    RANDOM = 0.5
    COSINE = 1


class Signal:

    def __init__(self):
        """
        Signal class constructor
        """
        self.sample_time = 2
        self.desc = 'unknown'
        self.sampling_rate = 60
        self.signal = None
        self.type = None

    @classmethod
    def generate_random(cls, sample_time, sampling_rate=60, desc='unknown'):
        """
        Create and return a Signal object filled with random signal
        :param sample_time: Overall time of the signal in second(s)
        :param sampling_rate: Rate the sampling of the signal in Hertz
        :param desc: Description of the signal
        :return: a Signal object
        """
        s = cls()
        s.sample_time = sample_time
        s.sampling_rate = sampling_rate
        s.check_for_invalid_input()
        s.desc = desc
        s.type = SignalType.RANDOM
        s.signal = np.random.rand(s.sampling_rate * s.sample_time) - 0.5
        s.check_for_invalid_signal(s, s.signal)
        return s

    @classmethod
    def generate_cosine(cls, sample_time, sampling_rate=60, desc='unknown'):
        """
        Create and return a Signal object filled with a cosine signal
        :param sample_time: Overall time of the signal in second(s)
        :param sampling_rate: Rate the sampling of the signal in Hertz
        :param desc: Description of the signal
        :return: a Signal object
        """
        s = cls()
        s.sample_time = sample_time
        s.sampling_rate = sampling_rate
        s.check_for_invalid_input()
        s.desc = desc
        s.type = SignalType.COSINE
        s.signal = np.cos(np.linspace(0,
                                      s.sample_time,
                                      s.sampling_rate * s.sample_time,
                                      endpoint=False) * np.pi * 10)
        s.check_for_invalid_signal(s, s.signal)
        return s

    def display(self):
        """
        Display a Signal object as a function and its associated frequencies
        :return: None
        """
        self.check_for_invalid_input()
        self.check_for_invalid_signal(self, self.signal)

        plt.subplot(1, 2, 1)
        plt.plot(np.linspace(0,
                             self.sample_time,
                             self.sampling_rate * self.sample_time,
                             endpoint=False),
                 self.signal,
                 label=self.desc)
        plt.xlabel('Time [s]')
        plt.ylabel('Signal Amplitude')

        plt.subplot(1, 2, 2)
        plt.stem(np.fft.fftfreq(len(self.signal)) * self.sampling_rate,
                 np.abs(self.get_frequencies()),
                 label=self.desc)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Frequency Magnitude')
        plt.xlim(-self.sampling_rate / 2, self.sampling_rate / 2)
        plt.show()

    def get_frequencies(self):
        """
        Compute the frequencies from the current object signal
        :return: frequency array as computed by numpy fft module
        """
        self.check_for_invalid_signal(self, self.signal)
        return np.fft.fft(self.signal)

    def compute_distance(self, s, sampling_type=ResamplingType.UP_SAMPLE):
        """
        Compute a difference measure between two signal objects
        :param sampling_type: resampling type for re-discretisation
        :param s: Signal object
        :return: the sum square difference
        """
        self.check_for_invalid_signals(s)
        self_signal_resampled, s_signal_resampled = self.get_re_discretised_signal(s, sampling_type)
        return np.sum(np.abs(self_signal_resampled - s_signal_resampled))

    def get_re_discretised_signal(self, s, sampling_type=ResamplingType.UP_SAMPLE):
        """
        Resample a signal to match another signal's length.
        :param sampling_type: Type of resampling (up/down sampling). Default is up-sample as less information is lost
        this way
        :param s: Signal object
        :return: the resampled signals
        """
        self.check_for_invalid_signals(s)
        if sampling_type is ResamplingType.UP_SAMPLE:
            return self.get_up_sampled_signals(s)
        return self.get_down_sampled_signals(s)

    def get_up_sampled_signals(self, s):
        """
        Up-sample a signal to match another signal's length.
        :param s: Signal object
        :return: A tuple with a resampled signal and an unchanged signalsignals
        """
        if len(self.signal) > len(s.signal):
            return self.signal, signal.resample(s.signal, len(self.signal))
        elif len(self.signal) < len(s.signal):
            return signal.resample(self.signal, len(s.signal)), s.signal
        return self.signal, s.signal

    def get_down_sampled_signals(self, s):
        """
        Down-sample a signal to match another signal's length.
        :param s: Signal object
        :return: A tuple with a resampled signal and an unchanged signal
        """
        if len(self.signal) > len(s.signal):
            return signal.resample(self.signal, len(s.signal)), s.signal
        elif len(self.signal) < len(s.signal):
            return self.signal, signal.resample(s.signal, len(self.signal))
        return self.signal, s.signal

    def get_similarity_pearson_correlation_coefficient(self, s, sampling_type=ResamplingType.UP_SAMPLE):
        """
        Calculate the similarity of two signals based on Pearson's correlation coefficient
        :param sampling_type: resampling type for re-discretisation
        :param s: Signal object
        :return: the similarity
        """
        self.check_for_invalid_signals(s)
        self_signal_resampled, s_signal_resampled = self.get_re_discretised_signal(s, sampling_type)
        return pearsonr(self_signal_resampled, s_signal_resampled)[0]

    def get_similarity_fourrier_transform(self, s, sampling_type=ResamplingType.UP_SAMPLE):
        """
        Calculate the similarity of two signals in the frequency domain by multiplying the two signals
        and summing the fourrier transform
        Shows if the signals share similar spectral shapes
        :param sampling_type: resampling type for re-discretisation
        :param s: Signal object
        :return: the similarity
        """
        self.check_for_invalid_signals(s)
        self_signal_resampled, s_signal_resampled = self.get_re_discretised_signal(s, sampling_type)
        product = self_signal_resampled * s_signal_resampled
        samples = max(len(self_signal_resampled), len(s_signal_resampled))
        return abs(np.sum(np.fft.fft(product)) / samples)


    def get_similarity_distance_time_warping(self, s, sampling_type=None):
        """
        Calculate the similarity of two signals using the Dynamic Time Warping algorithm
        Install: python -m pip install dtw
        :param sampling_type: resampling type for re-discretisation
        :param s: Signal object
        :return: the similarity
        """
        self.check_for_invalid_signals(s)
        euclidean_norm = lambda x, y: np.abs(x - y)
        if sampling_type is not None:
            self_signal, s_signal = self.get_re_discretised_signal(s, sampling_type)
        else:
            self_signal, s_signal = self.signal, s.signal

        d, _, _, _ = dtw(self_signal, s_signal, dist=euclidean_norm)

        return self.convert_distance_to_similarity(d, s, s_signal, self_signal)

    def convert_distance_to_similarity(self, d, s, s_signal, self_signal):
        max_samples = max(len(self_signal), len(s_signal))
        max_possible_value = self.get_max_possible_value(self_signal, s_signal, s)
        max_possible_distance = 2 * max_possible_value * max_samples
        return (max_possible_distance - d) / max_possible_distance

    def get_max_possible_value(self, self_signal, s_signal, s):
        """
        Get the max possible value a signal can have.
        If any of the signals' type is not defined, use the max value present in the signals
        :param self_signal: Main signal
        :param s_signal: Secondary signal
        :param s: Signal object
        :return: The max possible value
        """
        if self.type is None or s.type is None:
            return max(np.amax(self_signal), np.amax(s_signal))
        return max(self.type.value, s.type.value)

    def check_for_invalid_signals(self, s):
        """
        Validate both signals
        :param s: Signal object
        :raises TypeError: If None or non-numpy array
        :raises ValueError: if length is zero
        """
        self.check_for_invalid_signal(self, self.signal, "First signal")
        self.check_for_invalid_signal(self, s.signal, "Second signal")

    @staticmethod
    def check_for_invalid_signal(self, s, item="Signal"):
        """
        Validate a signal
        :param s: Signal object
        :param item: Used for a more descriptive exception message
        :raises TypeError: If None or non-numpy array
        :raises ValueError: if length is zero
        """
        if s is None:
            raise TypeError(item, " was not set")
        if not type(s) is np.ndarray:
            raise TypeError(item, " must be a numpy array")
        if (len(s)) == 0:
            raise ValueError(item, " can not be empty")

    def check_for_invalid_input(self):
        """
        Validate the sampling rate and sample time
        :raises TypeError: If None or non-int
        :raises ValueError: if less or equal to zero
        """
        self.validate_sample_time()
        self.validate_sampling_rate()

    def validate_sample_time(self):
        """
        Validate the sample time
        :raises TypeError: If None or non-int
        :raises ValueError: if less or equal to zero
        """
        self.check_valid_int(self, self.sample_time, "Sample time")

    def validate_sampling_rate(self):
        """
        Validate the sampling rate
        :raises TypeError: If None or non-int
        :raises ValueError: if less or equal to zero
        """
        self.check_valid_int(self, self.sampling_rate, "Sampling rate")

    @staticmethod
    def check_valid_int(self, number, item="Input"):
        """
        Validate a number
        :param number: The number to be validated
        :param item: Used for a more descriptive exception message
        :raises TypeError: If None or non-int
        :raises ValueError: if less or equal to zero
        """
        if number is None:
            raise TypeError(item, " was not set")
        if not isinstance(number, int):
            raise TypeError(item, " must be an integer")
        if number <= 0:
            raise ValueError(item, " must be greater than zero")
