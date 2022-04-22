import numpy as np


def classify_nn(training_filename, testing_filename, k):
    training_file = open(training_filename, 'r')
    training_lines = training_file.readlines()

    testing_file = open(testing_filename, 'r')
    testing_lines = testing_file.readlines()

    nearest_neighbour_count = k
    nearest_neighbours = []
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

    results_list = []
    # Apply formula to testing lines and iterate thru, keep k values in the nearest_neighbours.
    for i in formatted_testing_lines:
        digit_results = []
        class_results = []
        yes_tally = 0
        no_tally = 0

        for j in formatted_training_lines:
            # y, n, y, y, y, n, n, y, y, y, n, y, n, y, n, y, n, n, n, n, y, n
            a = np.array([float(x) for x in i[0:-1]])

            b = np.array([float(x) for x in j[0:-2]])
            temp = a - b
            dist = np.sqrt(np.dot(temp, temp.T))

            if len(digit_results) < nearest_neighbour_count:
                digit_results.append(dist)
                class_results.append(j[-1])

            else:
                counter = 0
                highest_neighbour = -1
                for x in digit_results:
                    if abs(x) > highest_neighbour:
                        highest_neighbour = abs(x)

                index_highest_neighbour = digit_results.index(highest_neighbour)
                if abs(dist) < abs(highest_neighbour):
                    class_results[index_highest_neighbour] = j[-1]
                    digit_results[index_highest_neighbour] = dist

        for x in class_results:
            if x == 'yes':
                yes_tally += 1
            else:
                no_tally += 1

        if yes_tally >= no_tally:
            results_list.append('yes')
        else:
            results_list.append('no')
    print(results_list)
    return results_list


print(classify_nn('training_data.csv', 'testing_data.csv', 3))
