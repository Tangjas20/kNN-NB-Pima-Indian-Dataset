import numpy as np
import pandas as pd


def organise_files(testing_data):
    testing_file = open(testing_data, 'r')
    testing_lines = testing_file.readlines()
    formatted_testing_lines = []

    for j in testing_lines:
        j = j.rstrip('\n')
        splitted_list = j.split(",")
        formatted_testing_lines.append(splitted_list)

    for i in formatted_testing_lines:
        for x in range(len(i)):
            i[x] = float(i[x])

    return formatted_testing_lines

def make_pandas_dataframe(training_filename):
    df = pd.read_csv(training_filename, header=None)
    df_yes = df[df.iloc[:,-1] == 'yes']
    df_yes = df_yes.assign(Index=range(len(df_yes))).set_index('Index')

    df_no = df[df.iloc[:,-1] == 'no']
    df_no = df_no.assign(Index=range(len(df_no))).set_index('Index')
    return df_yes, df_no

def mean(data):
    return sum(data)/float(len(data))

def stdev(data):
    return np.std(data)

def summarise_data(dataset):
    data_list = []
    for column in dataset.iloc[:,:-1]:
        col_mean = mean(dataset[column])
        col_stdev = stdev(dataset[column])
        col_count = len(dataset[column])
        tuple = (col_mean, col_stdev, col_count)
        data_list.append(tuple)

    return data_list

def calculate_probability(x, mean, stdev):
	exponent = np.exp(-((x-mean)**2 / (2 * stdev**2 )))
	return (1 / (np.sqrt(2 * np.pi) * stdev)) * exponent


def load_into_calculate_probability(testing_array, mean_stdev_tuple):
    counter = 0
    probabilities = []
    for i in testing_array:
        mean = mean_stdev_tuple[counter][0]
        stdev = mean_stdev_tuple[counter][1]
        probability = calculate_probability(i, mean, stdev)
        probabilities.append(probability)
        counter += 1

    return np.prod(probabilities)

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


def compare_probability_return_yes_no(formatted_testing, data_list_yes, data_list_no):
    result_list = []
    temp_list = []
    for i in formatted_testing:
        yes_probability = load_into_calculate_probability(i, data_list_yes)
        no_probability = load_into_calculate_probability(i, data_list_no)

        if yes_probability >= no_probability:
            temp_list.append('yes')
        else:
            temp_list.append('no')

    return temp_list


def classify_nb(training_filename, testing_filename):
    df_yes, df_no = make_pandas_dataframe(training_filename)
    data_list_yes = summarise_data(df_yes)
    data_list_no = summarise_data(df_no)
    formatted_testing = organise_files(testing_filename)
    result_list = compare_probability_return_yes_no(formatted_testing, data_list_yes, data_list_no)
    return result_list



print(classify_nb('training_data.csv', 'testing_data.csv'))
