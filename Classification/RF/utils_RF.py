'''
Created by Ming Li at 2019-01-30

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True):
    '''
    Return random subsets (with replacements) of the data
    :param X: X
    :param y: y
    :param n_subsets: number of subset for X, y
    :param replacements(boolean): sample with replacement, or without replacement
    :return: a list of subsets of data, each list element is a smaller list contains [X, y]
            [[x1,y1], [x2, y2], [x3, y3], ...]
    '''
    n_samples = np.shape(X)[0]
    # Concatenate x and y and do a random shuffle
    X_y = np.concatenate((X, y.reshape((1, len(y))).T), axis=1)
    np.random.shuffle(X_y)
    subsets = []

    # Uses 50% of training samples without replacements
    subsample_size = int(n_samples // 2)
    if replacements:
        subsample_size = n_samples      # 100% with replacements

    for _ in range(n_subsets):
        idx = np.random.choice(
            range(n_samples),
            size=np.shape(range(subsample_size)),
            replace=replacements)
        X = X_y[idx][:, :-1]
        y = X_y[idx][:, -1]
        subsets.append([X, y])
    return subsets