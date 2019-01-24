'''
Created by Ming Li at 2019-01-23

Feature: utils for decision tree

Description: utils for decision tree using numpy

Contact: ming.li2@columbia.edu
'''
import numpy as np

def entropy(col):
    '''
    :param col: np array
    :return: entropy of that np array
    '''
    _, counts = np.unique(col, return_counts=True)
    counts_proportion = np.array(counts) / sum(counts)
    entropy = np.sum(-1 * counts_proportion * np.log2(counts_proportion))
    return entropy

# ID3
def cal_info_gain(col_x, col_y):
    '''
    G(x, y) = H(x) - \sum{ \frac{|y_i|}{y} * H(y_i)}
    :param col_x: split by the col x
    :param col_y: the y as the labels
    :return: information gain for y split using x
    '''
    H_y = entropy(col_y)
    nums, counts = np.unique(col_x, return_counts=True)
    