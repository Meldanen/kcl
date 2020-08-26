from signal import Signal
from collections import defaultdict


if __name__ == "__main__":

    # First try to generate some signal
    try:
        s1 = Signal.generate_random(2, 60)
        s2 = Signal.generate_random(2, 60)
        s3 = Signal.generate_random(4, 30)
        s4 = Signal.generate_random(4, 60)
        s5 = Signal.generate_cosine(4, 60)
    except TypeError as type_error:
        print(type_error.args[0], ": ", type_error.args[1])
        raise type_error
    except ValueError as value_error:
        print(value_error.args[0], ": ", value_error.args[1])
        raise value_error

    # Display one signal and its associated frequency
    try:
        s1.display()
    except TypeError as type_error:
        print(type_error.args[0], ": ", type_error.args[1])
    except ValueError as value_error:
        print(value_error.args[0], ": ", value_error.args[1])

    try:
        s1.get_frequencies()
    except TypeError as type_error:
        print(type_error.args[0], ": ", type_error.args[1])
    except ValueError as value_error:
        print(value_error.args[0], ": ", value_error.args[1])

    # Compute distance between the first and other signals
    measures = list()
    # Here I used multiple try/catch clauses since one being fault doesn't mean we shouldn't add the rest
    try:
        measures.append(s1.compute_distance(s2))
    except TypeError as type_error:
        print(type_error.args[0], ": ", type_error.args[1])
    except ValueError as value_error:
        print(value_error.args[0], ": ", value_error.args[1])
    try:
        measures.append(s1.compute_distance(s3))
    except TypeError as type_error:
        print(type_error.args[0], ": ", type_error.args[1])
    except ValueError as value_error:
        print(value_error.args[0], ": ", value_error.args[1])
    try:
        measures.append(s1.compute_distance(s4))
    except TypeError as type_error:
        print(type_error.args[0], ": ", type_error.args[1])
    except ValueError as value_error:
        print(value_error.args[0], ": ", value_error.args[1])


    # Experiment 1: RT1 == RT2 and SR1 == SRS2
    cosine_signal = Signal.generate_cosine(2, 30)
    cosine_signal2 = Signal.generate_cosine(2, 30)
    print("----Experiment 1----")
    print("Sample time 1: ", cosine_signal.sample_time)
    print("Sample time 2: ", cosine_signal2.sample_time)
    print("Sampling rate 1: ", cosine_signal.sampling_rate)
    print("Sampling rate 2: ", cosine_signal2.sampling_rate)
    print("Pearson's: ", cosine_signal.get_similarity_pearson_correlation_coefficient(cosine_signal2))
    print("Fourrier: ", cosine_signal.get_similarity_fourrier_transform(cosine_signal2))
    print("DTW: ", cosine_signal.get_similarity_distance_time_warping(cosine_signal2))
    print("--------------------")

    # Experiment 2: RT1 != RT2 and SR1 == SRS2
    cosine_signal = Signal.generate_cosine(2, 30)
    cosine_signal2 = Signal.generate_cosine(3, 30)
    print("----Experiment 2----")
    print("Sample time 1: ", cosine_signal.sample_time)
    print("Sample time 2: ", cosine_signal2.sample_time)
    print("Sampling rate 1: ", cosine_signal.sampling_rate)
    print("Sampling rate 2: ", cosine_signal2.sampling_rate)
    print("Pearson's: ", cosine_signal.get_similarity_pearson_correlation_coefficient(cosine_signal2))
    print("Fourrier: ", cosine_signal.get_similarity_fourrier_transform(cosine_signal2))
    print("DTW: ", cosine_signal.get_similarity_distance_time_warping(cosine_signal2))
    print("--------------------")


    # Experiment 3: RT1 == RT2 and SR1 != SRS2
    cosine_signal = Signal.generate_cosine(2, 30)
    cosine_signal2 = Signal.generate_cosine(2, 67)
    print("----Experiment 3----")
    print("Sample time 1: ", cosine_signal.sample_time)
    print("Sample time 2: ", cosine_signal2.sample_time)
    print("Sampling rate 1: ", cosine_signal.sampling_rate)
    print("Sampling rate 2: ", cosine_signal2.sampling_rate)
    print("Pearson's: ", cosine_signal.get_similarity_pearson_correlation_coefficient(cosine_signal2))
    print("Fourrier: ", cosine_signal.get_similarity_fourrier_transform(cosine_signal2))
    print("DTW: ", cosine_signal.get_similarity_distance_time_warping(cosine_signal2))
    print("--------------------")


    # Experiment 4: RT1 != RT2 and SR1 != SRS2
    cosine_signal = Signal.generate_cosine(2, 30)
    cosine_signal2 = Signal.generate_cosine(3, 67)
    print("----Experiment 4----")
    print("Sample time 1: ", cosine_signal.sample_time)
    print("Sample time 2: ", cosine_signal2.sample_time)
    print("Sampling rate 1: ", cosine_signal.sampling_rate)
    print("Sampling rate 2: ", cosine_signal2.sampling_rate)
    print("Pearson's: ", cosine_signal.get_similarity_pearson_correlation_coefficient(cosine_signal2))
    print("Fourrier: ", cosine_signal.get_similarity_fourrier_transform(cosine_signal2))
    print("DTW: ", cosine_signal.get_similarity_distance_time_warping(cosine_signal2))
    print("--------------------")


    # Experiment 5: RT1 = 2*RT2 and SR1 == SRS2
    cosine_signal = Signal.generate_cosine(2, 30)
    cosine_signal2 = Signal.generate_cosine(16, 30)
    print("----Experiment 5----")
    print("Sample time 1: ", cosine_signal.sample_time)
    print("Sample time 2: ", cosine_signal2.sample_time)
    print("Sampling rate 1: ", cosine_signal.sampling_rate)
    print("Sampling rate 2: ", cosine_signal2.sampling_rate)
    print("Pearson's: ", cosine_signal.get_similarity_pearson_correlation_coefficient(cosine_signal2))
    print("Fourrier: ", cosine_signal.get_similarity_fourrier_transform(cosine_signal2))
    print("DTW: ", cosine_signal.get_similarity_distance_time_warping(cosine_signal2))
    print("--------------------")

    # Experiment 6: RT1 == RT2 and SR1 == SRS2 with noise
    cosine_signal = Signal.generate_cosine(2, 30)
    cosine_signal2 = Signal.generate_cosine(2, 30)
    averages = defaultdict(int)
    iterations = 10
    for i in range(0, iterations):
        cosine_signal2 = Signal.generate_cosine(2, 30)
        noise = Signal.generate_random(2, 30).signal;
        cosine_signal2.signal = cosine_signal2.signal + noise
        averages['Pearson'] += cosine_signal.get_similarity_pearson_correlation_coefficient(cosine_signal2)
        averages['Fourrier'] += cosine_signal.get_similarity_fourrier_transform(cosine_signal2)
        averages['DTW'] += cosine_signal.get_similarity_distance_time_warping(cosine_signal2)
    averages = dict(map(lambda kv: (kv[0], kv[1]/iterations), averages.items()))
    print("----Experiment 6----")
    print("Sample time 1: ", cosine_signal.sample_time)
    print("Sample time 2: ", cosine_signal2.sample_time)
    print("Sampling rate 1: ", cosine_signal.sampling_rate)
    print("Sampling rate 2: ", cosine_signal2.sampling_rate)
    print("Pearson's: ", averages['Pearson'])
    print("Fourrier: ", averages['Fourrier'])
    print("DTW: ", averages['DTW'])
    print("--------------------")


    # Experiment 7: RT1 != RT2 and SR1 != SRS2
    averages = defaultdict(int)
    iterations = 10
    for i in range(0, iterations):
        random_signal = Signal.generate_random(2, 30)
        random_signal2 = Signal.generate_random(3, 45)
        averages['Pearson'] += random_signal.get_similarity_pearson_correlation_coefficient(random_signal2)
        averages['Fourrier'] += random_signal.get_similarity_fourrier_transform(random_signal2)
        averages['DTW'] += random_signal.get_similarity_distance_time_warping(random_signal2)
    averages = dict(map(lambda kv: (kv[0], kv[1]/iterations), averages.items()))
    print("----Experiment 7----")
    print("Sample time 1: ", random_signal.sample_time)
    print("Sample time 2: ", random_signal2.sample_time)
    print("Sampling rate 1: ", random_signal.sampling_rate)
    print("Sampling rate 2: ", random_signal2.sampling_rate)
    print("Pearson's: ", averages['Pearson'])
    print("Fourrier: ", averages['Fourrier'])
    print("DTW: ", averages['DTW'])
    print("--------------------")

    # Experiment 8: RT1 != RT2 and SR1 == SRS2
    averages = defaultdict(int)
    iterations = 10
    for i in range(0, iterations):
        random_signal = Signal.generate_random(2, 30)
        random_signal2 = Signal.generate_random(3, 30)
        averages['Pearson'] += random_signal.get_similarity_pearson_correlation_coefficient(random_signal2)
        averages['Fourrier'] += random_signal.get_similarity_fourrier_transform(random_signal2)
        averages['DTW'] += random_signal.get_similarity_distance_time_warping(random_signal2)
    averages = dict(map(lambda kv: (kv[0], kv[1]/iterations), averages.items()))
    print("----Experiment 8----")
    print("Sample time 1: ", random_signal.sample_time)
    print("Sample time 2: ", random_signal2.sample_time)
    print("Sampling rate 1: ", random_signal.sampling_rate)
    print("Sampling rate 2: ", random_signal2.sampling_rate)
    print("Pearson's: ", averages['Pearson'])
    print("Fourrier: ", averages['Fourrier'])
    print("DTW: ", averages['DTW'])
    print("--------------------")

    # Experiment 9: RT1 == RT2 and SR1 != SRS2
    averages = defaultdict(int)
    iterations = 10
    for i in range(0, iterations):
        random_signal = Signal.generate_random(2, 30)
        random_signal2 = Signal.generate_random(2, 54)
        averages['Pearson'] += random_signal.get_similarity_pearson_correlation_coefficient(random_signal2)
        averages['Fourrier'] += random_signal.get_similarity_fourrier_transform(random_signal2)
        averages['DTW'] += random_signal.get_similarity_distance_time_warping(random_signal2)
    averages = dict(map(lambda kv: (kv[0], kv[1]/iterations), averages.items()))
    print("----Experiment 9----")
    print("Sample time 1: ", random_signal.sample_time)
    print("Sample time 2: ", random_signal2.sample_time)
    print("Sampling rate 1: ", random_signal.sampling_rate)
    print("Sampling rate 2: ", random_signal2.sampling_rate)
    print("Pearson's: ", averages['Pearson'])
    print("Fourrier: ", averages['Fourrier'])
    print("DTW: ", averages['DTW'])
    print("--------------------")


