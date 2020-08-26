import unittest
from signal import Signal
from signal import ResamplingType
import numpy as np


class TestSignal(unittest.TestCase):

    def test_repr(self):
        self.assertIsNotNone(repr(Signal()))

    """
    Need to test whether a valid sample time was passed in
    Values less or equal to zero are invalid because time can't be negative
    Using a less or equal to zero value will lead to a negative/zero signal length
    Values that are not set (None) or that are not ints are invalid as well
    """
    def test_generate_random_invalid_sample_time(self):
        with self.assertRaises(ValueError):
            Signal.generate_random(0, 60)
        with self.assertRaises(ValueError):
            Signal.generate_random(-2, 60)
        with self.assertRaises(TypeError):
            Signal.generate_random(2.0, 60)
        with self.assertRaises(TypeError):
            Signal.generate_random(None, 60)
        with self.assertRaises(TypeError):
            Signal.generate_random("I shouldn't be a string", 60)

    """
    Need to test whether a valid sampling rate was passed in
    Values less or equal to zero are invalid because a sampling rate can't be negative
    Using a less or equal to zero value will lead to a negative/zero signal length
    Values that are not set (None) or that are not ints are invalid as well
    """
    def test_generate_random_invalid_sampling_rate(self):
        with self.assertRaises(ValueError):
            Signal.generate_random(2, -60)
        with self.assertRaises(ValueError):
            Signal.generate_random(2, 0)
        with self.assertRaises(TypeError):
            Signal.generate_random(2, 60.0)
        with self.assertRaises(TypeError):
            Signal.generate_random(2, None)
        with self.assertRaises(TypeError):
            Signal.generate_random(2, "I shouldn't be a string either")

    """
    Need to test whether a valid signal is generated
    Signal's length needs to be equal to sample time * sampling rate
    Signal must contain only numeric elements
    """
    def test_generate_random_generates_valid_signal(self):
        random_signal = Signal.generate_random(2, 60)
        signal = random_signal.signal
        self.assertTrue(len(signal) == 120)
        self.assertTrue(all(isinstance(x, float) for x in signal))

    """
    Need to test whether a valid sample time was passed in
    Values less or equal to zero are invalid because time can't be negative
    Using a less or equal to zero value will lead to a negative/zero signal length
    Values that are not set (None) or that are not ints are invalid as well
    """
    def test_generate_cosine_invalid_sample_time(self):
        with self.assertRaises(ValueError):
            Signal.generate_cosine(0, 60)
        with self.assertRaises(ValueError):
            Signal.generate_cosine(-2, 60)
        with self.assertRaises(TypeError):
            Signal.generate_cosine(2.0, 60)
        with self.assertRaises(TypeError):
            Signal.generate_cosine(None, 60)
        with self.assertRaises(TypeError):
            Signal.generate_cosine("I shouldn't be a string", 60)

    """
    Need to test whether a valid sampling rate was passed in
    Values less or equal to zero are invalid because a sampling rate can't be negative
    Using a less or equal to zero value will lead to a negative/zero signal length
    Values that are not set (None) or that are not ints are invalid as well
    """
    def test_generate_cosine_invalid_sampling_rate(self):
        with self.assertRaises(ValueError):
            Signal.generate_cosine(2, -60)
        with self.assertRaises(ValueError):
            Signal.generate_cosine(2, 0)
        with self.assertRaises(TypeError):
            Signal.generate_cosine(2, 60.0)
        with self.assertRaises(TypeError):
            Signal.generate_cosine(2, None)
        with self.assertRaises(TypeError):
            Signal.generate_cosine(2, "I shouldn't be a string either")

    """
    Need to test whether a valid signal is generated
    Signal's length needs to be equal to sample time * sampling rate
    Signal must contain only numeric elements
    """
    def test_generate_cosine_generates_valid_signal(self):
        cosine_signal = Signal.generate_cosine(2, 60)
        signal = cosine_signal.signal
        self.assertTrue(len(signal) == 120)
        self.assertTrue(all(isinstance(x, float) for x in signal))

    """
    Need to test whether a valid signal is supplied. A valid and non-empty frequency is required in order to plot 
    the signal
    Signal needs to be not None
    Signal needs to be not empty
    Signal needs to be an array
    """
    def test_get_frequencies_invalid_signal(self):
        empty_signal = Signal()
        with self.assertRaises(TypeError):
            empty_signal.get_frequencies()
        with self.assertRaises(ValueError):
            empty_signal.signal = np.array([])
            empty_signal.get_frequencies()
        with self.assertRaises(TypeError):
            empty_signal.signal = 1
            empty_signal.get_frequencies()

    """
    Need to test that a valid list of frequencies are returned when a valid signal is supplied
    A valid and non-empty frequency is required in order to plot the signal
    The total number of frequencies should be equal to sample time * sampling rate 
    """
    def test_get_frequencies_valid_signal(self):
        cosine_signal = Signal.generate_cosine(4, 60)
        cosine_frequencies = cosine_signal.get_frequencies()
        self.assertTrue(cosine_frequencies.size == 240)

        random_signal = Signal.generate_random(2, 100)
        random_frequencies = random_signal.get_frequencies()
        self.assertTrue(random_frequencies.size == 200)

    """
    Need to test whether the two signals are valid for random signals. A valid and non-empty signal is required
    in order to properly compute the distance between two signals
    Signals must not be None or empty
    """
    def test_compute_distance_invalid_random_signals(self):
        # Test with the object being a None
        with self.assertRaises(TypeError):
            random_signal = Signal()
            random_signal2 = Signal()
            random_signal.compute_distance(random_signal2)

        # Test with the object's signal being a None
        with self.assertRaises(TypeError):
            random_signal = Signal.generate_random(2, 30)
            random_signal2 = Signal.generate_random(2, 60)
            random_signal.signal = None
            random_signal2.signal = None
            random_signal.compute_distance(random_signal2)

        # Test with the object's signal being empty
        with self.assertRaises(ValueError):
            random_signal = Signal.generate_random(2, 30)
            random_signal2 = Signal.generate_random(2, 60)
            random_signal.signal = np.array([])
            random_signal.compute_distance(random_signal2)
        with self.assertRaises(ValueError):
            random_signal = Signal.generate_random(2, 30)
            random_signal2 = Signal.generate_random(2, 60)
            random_signal2.signal = np.array([])
            random_signal.compute_distance(random_signal2)

        # Test with the object's signal not being a list (i.e. just an int)
        with self.assertRaises(TypeError):
            random_signal = Signal.generate_random(2, 30)
            random_signal2 = Signal.generate_random(2, 60)
            random_signal.signal = 1
            random_signal.compute_distance(random_signal2)
        with self.assertRaises(TypeError):
            random_signal = Signal.generate_random(2, 30)
            random_signal2 = Signal.generate_random(2, 60)
            random_signal2.signal = 2
            random_signal.compute_distance(random_signal2)

    """
    Need to test whether the two signals are valid for cosine signals. A valid and non-empty signal is required
    in order to properly compute the distance between two signals
    Signals must not be None or empty
    """
    def test_compute_distance_invalid_cosine_signals(self):
        # Test with the object being a None
        with self.assertRaises(TypeError):
            cosine_signal = Signal()
            cosine_signal2 = Signal()
            cosine_signal.compute_distance(cosine_signal2)

        # Test with the object's signal being a None
        with self.assertRaises(TypeError):
            cosine_signal = Signal.generate_cosine(2, 30)
            cosine_signal2 = Signal.generate_cosine(2, 60)
            cosine_signal.signal = None
            cosine_signal2.signal = None
            cosine_signal.compute_distance(cosine_signal2)

        # Test with the object's signal being empty
        with self.assertRaises(ValueError):
            cosine_signal = Signal.generate_cosine(2, 30)
            cosine_signal2 = Signal.generate_cosine(2, 60)
            cosine_signal.signal = np.array([])
            cosine_signal.compute_distance(cosine_signal2)
        with self.assertRaises(ValueError):
            cosine_signal = Signal.generate_cosine(2, 30)
            cosine_signal2 = Signal.generate_cosine(2, 60)
            cosine_signal2.signal = np.array([])
            cosine_signal.compute_distance(cosine_signal2)

        # Test with the object's signal not being a list (i.e. just an int)
        with self.assertRaises(TypeError):
            cosine_signal = Signal.generate_cosine(2, 30)
            cosine_signal2 = Signal.generate_cosine(2, 60)
            cosine_signal.signal = 1
            cosine_signal.compute_distance(cosine_signal2)
        with self.assertRaises(TypeError):
            cosine_signal = Signal.generate_cosine(2, 30)
            cosine_signal2 = Signal.generate_cosine(2, 60)
            cosine_signal2.signal = 2
            cosine_signal.compute_distance(cosine_signal2)

    """
    Need to test whether the distance is computed correctly for valid input
    We'll test various combinations (between different kinds of signals) to make sure that they are compatible.
    Comparing equal signals should have zero distance
    """
    def test_compute_distance_compatible(self):
        # Test cosine vs cosine
        cosine_signal = Signal.generate_cosine(2, 60)
        cosine_signal2 = Signal.generate_cosine(7, 43)
        self.assertAlmostEqual(cosine_signal.compute_distance(cosine_signal), 0.0)
        self.assertAlmostEqual(cosine_signal.compute_distance(cosine_signal2), 244.05038, 5)

        # Test random vs random
        random_signal = Signal.generate_random(2, 60)
        random_signal2 = Signal.generate_random(2, 120)
        self.assertAlmostEqual(random_signal.compute_distance(random_signal), 0.0)
        self.assertTrue(random_signal.compute_distance(random_signal2) > 0.0)

        # Test cosine vs random
        self.assertTrue(cosine_signal.compute_distance(random_signal) > 0.0)

    """
    Using invalid (None/empty) signals should raise Type/Value Error exceptions as they can't be used for resampling
    """
    def test_re_discretise_signal_invalid_signals(self):
        # Test for None
        with self.assertRaises(TypeError):
            random_signal = Signal()
            cosine_signal = Signal.generate_cosine(3, 60)
            random_signal.get_re_discretised_signal(cosine_signal)

        # Test for None
        with self.assertRaises(TypeError):
            random_signal = Signal.generate_random(2, 60)
            cosine_signal = Signal()
            random_signal.get_re_discretised_signal(cosine_signal)

        # Test for empty
        with self.assertRaises(ValueError):
            random_signal = Signal.generate_random(2, 60)
            random_signal.signal = np.array([])
            cosine_signal = Signal.generate_cosine(3, 60)
            random_signal.get_re_discretised_signal(cosine_signal)

        # Test for empty
        with self.assertRaises(ValueError):
            random_signal = Signal.generate_random(2, 60)
            cosine_signal = Signal.generate_cosine(3, 60)
            cosine_signal.signal = np.array([])
            random_signal.get_re_discretised_signal(cosine_signal)

    """
    Valid signals should successfully be resampled to allow us to compare them
    The resampled signal should be different from the original
    Since we're up-sampling, the larger signal should remain the same
    """
    def test_re_discretise_signal_valid_signal_up_sample(self):
        random_signal = Signal.generate_random(2, 60)
        cosine_signal = Signal.generate_cosine(3, 60)
        random_resampled, cosine_resampled = random_signal.get_re_discretised_signal(cosine_signal)
        self.assertEqual(len(cosine_resampled), 180)
        self.assertEqual(len(random_resampled), len(cosine_resampled))
        self.assertFalse(np.array_equal(random_signal.signal, random_resampled))
        self.assertTrue(np.array_equal(cosine_signal.signal, cosine_resampled))

    """
    Valid signals should successfully be resampled to allow us to compare them
    The resampled signal should be different from the original
    Since we're down-sampling, the smaller signal should remain the same
    """
    def test_re_discretise_signal_valid_signal_down_sample(self):
        random_signal = Signal.generate_random(2, 60)
        cosine_signal = Signal.generate_cosine(3, 60)
        random_resampled, cosine_resampled = random_signal.get_re_discretised_signal(cosine_signal, ResamplingType.DOWN_SAMPLE)
        self.assertEqual(len(cosine_resampled), 120)
        self.assertEqual(len(random_resampled), len(cosine_resampled))
        self.assertTrue(np.array_equal(random_signal.signal, random_resampled))
        self.assertFalse(np.array_equal(cosine_signal.signal, cosine_resampled))

    """
    The signal that will be resampled should not change if it already has the same length as the main signal
    """
    def test_re_discretise_signal_does_not_change_if_same_length(self):
        random_signal = Signal.generate_random(2, 60)
        cosine_signal = Signal.generate_cosine(2, 60)
        random_resampled, cosine_resampled = random_signal.get_re_discretised_signal(cosine_signal)
        self.assertEqual(random_signal.signal.shape[0], len(cosine_resampled))
        self.assertTrue(np.array_equal(cosine_signal.signal, cosine_resampled))
        self.assertTrue(np.array_equal(random_signal.signal, random_resampled))

        random_resampled, cosine_resampled = random_signal.get_re_discretised_signal(cosine_signal, ResamplingType.DOWN_SAMPLE)
        self.assertEqual(random_signal.signal.shape[0], len(cosine_resampled))
        self.assertTrue(np.array_equal(cosine_signal.signal, cosine_resampled))
        self.assertTrue(np.array_equal(random_signal.signal, random_resampled))

    """
    Test function for the cross correlation similarity metric
    """
    def test_similarity_pearson_correlation_coefficient(self):
        # Test 1: Two equal signals should be 100% correlated
        random_signal = Signal.generate_random(2, 60)
        random_similarity = random_signal.get_similarity_pearson_correlation_coefficient(random_signal)
        self.assertAlmostEqual(random_similarity, 1.0)
        cosine_signal = Signal.generate_cosine(2, 30)
        cosine_similarity = cosine_signal.get_similarity_pearson_correlation_coefficient(cosine_signal)
        self.assertAlmostEqual(cosine_similarity, 1.0)

        # Test 2: Random signals should probably not be too similar or dissimilar
        random_signal = Signal.generate_random(2, 60)
        random_signal2 = Signal.generate_random(2, 100)
        random_similarity = random_signal.get_similarity_pearson_correlation_coefficient(random_signal2)
        self.assertTrue(-1 < random_similarity < 1)
        random_signal = Signal.generate_random(2, 60)
        random_signal2 = Signal.generate_random(4, 60)
        random_similarity = random_signal.get_similarity_pearson_correlation_coefficient(random_signal2)
        self.assertTrue(-1 < random_similarity < 1)
        random_signal = Signal.generate_random(2, 60)
        random_signal2 = Signal.generate_random(3, 100)
        random_similarity = random_signal.get_similarity_pearson_correlation_coefficient(random_signal2)
        self.assertTrue(-1 < random_similarity < 1)

        # Test 3: Two cosine signals with the same sample time should be highly correlated given that the signal is
        # resampled
        cosine_signal = Signal.generate_cosine(2, 30)
        cosine_signal2 = Signal.generate_cosine(2, 1232)
        cosine_similarity = cosine_signal.get_similarity_pearson_correlation_coefficient(cosine_signal2)
        self.assertAlmostEqual(cosine_similarity, 1.0)

        # Test 4: Two cosine signals with different sample time should be highly de-correlated
        cosine_signal = Signal.generate_cosine(2, 30)
        cosine_signal2 = Signal.generate_cosine(4, 30)
        cosine_similarity = cosine_signal.get_similarity_pearson_correlation_coefficient(cosine_signal2)
        self.assertAlmostEqual(cosine_similarity, 0.0)
        cosine_signal = Signal.generate_cosine(2, 40)
        cosine_signal2 = Signal.generate_cosine(4, 80)
        cosine_similarity = cosine_signal.get_similarity_pearson_correlation_coefficient(cosine_signal2)
        self.assertAlmostEqual(cosine_similarity, 0.0)

    """
    Test function for the fourrier transform product similarity metric. This is based on the frequency domain
    """
    def test_similarity_fourrier_transform(self):

        # Test 1: Two equal cosine signals should be 100% similar
        cosine_signal = Signal.generate_cosine(2, 30)
        cosine_similarity = cosine_signal.get_similarity_fourrier_transform(cosine_signal)
        self.assertAlmostEqual(cosine_similarity, 1.0)

        # Test 2: Cosine signals are pretty similar. Due to resampling and the fact that this method measures difference
        # in frequency, two different ones should still be similar
        cosine_signal = Signal.generate_cosine(2, 30)
        cosine_signal2 = Signal.generate_cosine(4, 433)
        cosine_similarity = cosine_signal.get_similarity_fourrier_transform(cosine_signal2)
        self.assertAlmostEqual(cosine_similarity, 1)

        # Test 3: Random signals should probably not be too similar or dissimilar
        random_signal = Signal.generate_random(2, 60)
        random_signal2 = Signal.generate_random(3, 105)
        random_similarity = random_signal.get_similarity_fourrier_transform(random_signal2)
        self.assertTrue(0 < random_similarity < 1)

    """
    Test function for the fourrier transform product similarity metric
    """
    def test_similarity_distance_time_warping(self):

        # Test 1: Two equal signals should be 100% similar
        random_signal = Signal.generate_random(2, 30)
        random_similarity = random_signal.get_similarity_distance_time_warping(random_signal)
        self.assertAlmostEqual(random_similarity, 1.0)
        cosine_signal = Signal.generate_cosine(2, 30)
        cosine_similarity = cosine_signal.get_similarity_distance_time_warping(cosine_signal)
        self.assertAlmostEqual(cosine_similarity, 1.0)

        # Test 2: Cosine signals are pretty similar. Due to resampling, two different ones should still be similar but
        # not measured as being the same
        cosine_signal = Signal.generate_cosine(2, 40)
        cosine_signal2 = Signal.generate_cosine(4, 40)
        cosine_similarity = cosine_signal.get_similarity_distance_time_warping(cosine_signal2)
        self.assertTrue(cosine_similarity > 0.80)
        cosine_signal = Signal.generate_cosine(2, 40)
        cosine_signal2 = Signal.generate_cosine(2, 80)
        cosine_similarity = cosine_signal.get_similarity_distance_time_warping(cosine_signal2)
        self.assertTrue(cosine_similarity > 0.80)
        cosine_signal = Signal.generate_cosine(2, 40)
        cosine_signal2 = Signal.generate_cosine(4, 80)
        cosine_similarity = cosine_signal.get_similarity_distance_time_warping(cosine_signal2)
        self.assertTrue(cosine_similarity > 0.80)

        # Test 3: Random signals should probably not be too similar or dissimilar
        random_signal = Signal.generate_random(2, 60)
        random_signal2 = Signal.generate_random(3, 105)
        random_similarity = random_signal.get_similarity_distance_time_warping(random_signal2)
        self.assertTrue(0 < random_similarity < 1)


if __name__ == '__main__':
    unittest.main()
