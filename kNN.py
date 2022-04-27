import numpy as np


def organise_files(training_data, testing_data):
    training_file = open(training_data, 'r')
    training_lines = training_file.readlines()

    testing_file = open(testing_data, 'r')
    testing_lines = testing_file.readlines()

    formatted_training_lines = []
    formatted_testing_lines = []

    for i in training_lines:
        i = i.rstrip('\n')
        split_list = i.split(",")
        formatted_training_lines.append(split_list)

    for j in testing_lines:
        j = j.rstrip('\n')
        splitted_list = j.split(",")
        formatted_testing_lines.append(splitted_list)

    for i in formatted_training_lines:
        for x in range(len(i) - 1):
            i[x] = float(i[x])

    for i in formatted_testing_lines:
        for x in range(len(i)):
            i[x] = float(i[x])

    return formatted_training_lines, formatted_testing_lines


def calculate_euclidean_distance(array1, array2):
    a = np.array(array1)
    b = np.array(array2[:-1])
    temp = a - b
    dist = np.sqrt(np.dot(temp.T, temp))
    dist = round(dist, 4)

    return dist


def min_k_dist(dist_results, k, training_filename):
    smallest_indexes = []
    k_yes_no_list = []
    sorted_dist_results = sorted(dist_results)[:k]

    for x in sorted_dist_results:
        smallest_indexes.append(dist_results.index(x))

    for x in smallest_indexes:
        k_yes_no_list.append(training_filename[x][-1])

    return k_yes_no_list


def tally_yes_no(k_yes_no_list):
    n_tally = 0
    y_tally = 0
    for x in k_yes_no_list:
        if x == 'yes':
            y_tally += 1
        elif x == 'no':
            n_tally += 1
    if y_tally >= n_tally:
        return 'yes'
    else:
        return 'no'


def classify_nn(training_filename, testing_filename, k):
    training, testing = organise_files(training_filename, testing_filename)
    results_list = []

    for i in testing:
        dist_results = []
        for j in training:

            dist_results.append(calculate_euclidean_distance(i, j))
        min_list = min_k_dist(dist_results, k, training)
        results_list.append(tally_yes_no(min_list))

    return results_list


correct_result = ['yes', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'no',
                  'yes', 'no', 'no', 'no', 'no', 'yes', 'no']
counter = 0
i = 0
index_not_match = []
results_list = classify_nn('training_data.csv', 'testing_data.csv', 5)
while i < (len(correct_result) - 1):
    if correct_result[i] == results_list[i]:
        counter += 1
    else:
        index_not_match.append(i)
    print(results_list[i])
    i += 1

print(index_not_match)
print(results_list)
print("accuracy", counter / len(correct_result))

