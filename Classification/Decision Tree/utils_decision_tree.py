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
def cal_infor_gain(col_x, col_y):
    '''
    G(x, y) = H(x) - \sum{ \frac{|y_i|}{y} * H(y_i)}
    :param col_x: split by the col x
    :param col_y: the y as the labels
    :return: information gain for y split using x
    '''
    H_y = entropy(col_y)
    nums, counts = np.unique(col_x, return_counts=True)
    H_y_x = 0
    for x_i in nums:
        subset_x_i = col_y[col_x == x_i]
        x_i_proportion = counts/len(col_x)
        H_y_x += x_i_proportion * entropy(subset_x_i)
    infor_gain = H_y - H_y_x
    return infor_gain

# C4.5
def cal_infor_gain_ratio(col_x, col_y):
    '''
    Gain_ratio(x, y) = \frac{ Gain(x, y) }{ IV(col_x) }
    x_i_ratio = \frac{|x_i|}{|x|}
    IV(col_x) = -\sum{ x_i_ratio * log_{2}x_i_ratio }
    :param col_x: split by the col x
    :param col_y: the y as the labels
    :return: information gain ratio for y split using x
    '''
    IV_x = 0
    nums, counts = np.unique(col_x, return_counts=True)
    counts_proportion = np.array(counts) / sum(counts)
    for proportion in counts_proportion:
        IV_x += -1 * proportion * log2(proportion)
    infor_gain_ratio = cal_infor_gain(col_x, col_y) / IV_x
    return infor_gain_ratio


# CART
def cal_Gini(col_x):
    nums, counts = np.unique(col_x)
    counts_proportion = np.array(counts) / len(col_x)
    gini = 1 - np.sum(counts_proportion ** 2)
    return gini

def cal_Gini_Index(col_x, col_y):
    '''
    Gini_index(x, y) = \sum{ x_i_proportion * Gini (col_x[x_i]) }
    :param col_x: split by the col x
    :param col_y: the y as the labels
    :return: the Gini index of feature col_x
    '''
    nums, counts = np.unique(col_x, return_counts=True)
    counts_proportion = np.array(counts) / len(col_x)
    gini_index = 0
    for x_i in nums:
        gini_index += counts_proportion * cal_Gini(col_y[col_x == x_i])
    return gini_index


    
        