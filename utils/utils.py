'''
Created by Ming Li at 2019-01-24

Feature: utils for all the algorithm and data process part

Description:

Contact: ming.li2@columbia.edu
'''

from __future__ import division
from itertools import combinations_with_replacement
import numpy as np
import math
import sys

def shuffle_data(X, y, seed = None):
    '''
    random shuffle of the input data, X and label
    :param X: input X
    :param y: input y
    :param seed: seed for np.random.seed()
    :return: the shuffled dataset with X and y
    '''
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]


def standardize(X):
    '''
    standardize the matrix x, by column axis
    :param X: input X matrix
    :return: standardized X matrix
    '''
    X_std = X
    mean = X.mean(axis = 0)
    std = X.std(axis = 0)
    col_num = np.shape(X)[1]
    for col in range(col_num):
        if std[col]:
            X_std[:, col] = (X_std[:, col] - mean[col]) / std[col]
    return X_std



def train_test_split(X, y, test_size=0.3, shuffle=True, seed=None):
    """ Split the data into train and test sets """
    if shuffle:
        X, y = shuffle_data(X, y, seed)
    # Split the training data from test data in the ratio specified in
    # test_size
    split_i = len(y) - int(len(y) // (1 / test_size))
    X_train, X_test = X[:split_i], X[split_i:]
    y_train, y_test = y[:split_i], y[split_i:]

    return X_train, X_test, y_train, y_test


def k_fold_cross_validation_sets(X, y, k, shuffle=True):
    """ Split the data into k sets of training / test data """
    if shuffle:
        X, y = shuffle_data(X, y)

    n_samples = len(y)
    left_overs = {}
    n_left_overs = (n_samples % k)
    if n_left_overs != 0:
        left_overs["X"] = X[-n_left_overs:]
        left_overs["y"] = y[-n_left_overs:]
        X = X[:-n_left_overs]
        y = y[:-n_left_overs]

    X_split = np.split(X, k)
    y_split = np.split(y, k)
    sets = []
    for i in range(k):
        X_test, y_test = X_split[i], y_split[i]
        X_train = np.concatenate(X_split[:i] + X_split[i + 1:], axis=0)
        y_train = np.concatenate(y_split[:i] + y_split[i + 1:], axis=0)
        sets.append([X_train, X_test, y_train, y_test])

    # Add left over samples to last set as training samples
    if n_left_overs != 0:
        np.append(sets[-1][0], left_overs["X"], axis=0)
        np.append(sets[-1][2], left_overs["y"], axis=0)

    return np.array(sets)