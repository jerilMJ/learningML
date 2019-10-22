'''
Program to read data for math operators identification. The compressed data
made using the dataset_maker is loaded and unpacked then returned to the 
calling program.
'''

import pickle
import gzip
import numpy as np


def load_data():
    '''
    Returns training data and test data as a tuple. They are lists that
    contain the image as a numpy ndarray and the corresponding label.
    The compressed file is first opened using gzip and then contents 
    are loaded and unpacked using pickle.
    The length of each set is printed for validation of the dataset.
    '''
    f = gzip.open('../dataset/zipped.pkl.gz', 'rb')
    training_data, test_data = pickle.load(f)
    print("Training: ", len(training_data[0]), len(training_data[1]))
    print("Test: ", len(test_data[0]), len(test_data[1]))
    f.close()
    return (training_data, test_data)


def load_data_wrapper():
    '''
    Return training data and test data as a tuple in a format that can
    be used by the program. 
    Operators are arranged in the following order:
    plus    minus   multiply    divide
    eg: If plus is the label, then the corresponding number is 0. So the
    vectorized result would be 1 0 0 0.
    The inputs and targets are zipped together before they are returned.
    '''
    tr_d, te_d = load_data()
    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])
    return (training_data, test_data)


def vectorized_result(label):
    '''
    Return a list of 1s and 0s corresponding to the correct activation
    of the output layer neurons for each input.
    '''
    e = np.zeros((4, 1))
    e[label] = 1.0
    return e
