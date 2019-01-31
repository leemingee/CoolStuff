'''
Created by Ming Li at 2019-01-30

Feature:
- train test split
- k folder split
- cross validation evaluation
- algorithm evaluation

Description: utils for the classification

Contact: ming.li2@columbia.edu
'''
import numpy as np
import random

def shuffle_data(X, y, random_state):
    '''shuffle for X and y'''
    if random_state:
        '''但是numpy.random.seed()不是线程安全的，
        如果程序中有多个线程最好使用numpy.random.RandomState
        实例对象来创建或者使用random.seed()来设置相同的随机数种子。'''
        np.random.RandomState(random_state)
    assert X.shape[0] == len(y), 'X and y first dim should be the same!'
    idx = np.arange(len(y))
    new_idx = np.random.shuffle(idx)
    return X[new_idx], y[new_idx]
    

def train_test_split(X, y, **params):
    '''
    
    :param array: the dataset to be splitted
    :param params: the params dict to be used for split
    :return: the list of splitted dataset
    '''
    assert X.shape[0] != 0, "At least one X required as input"
    assert len(y) != 0, 'At least one Y required as input'
    assert X.shape[0] == len(y), 'X and y first dimension should be the same!'
    test_size = params.pop('test_size', 'default')
    random_state = params.pop('random_state', None)
    shuffle = params.pop('shuffle', True)
    
    if params:
        raise TypeError("Invalid parameters passed: %s" % str(params))
    
    if test_size == 'default':
        print('using the default test split size of 0.25')
        test_size = 0.25
        
    if shuffle:
        X, y = shuffle_data(X, y, random_state)

    split_i = len(y) - int(len(y) * test_size)
    X_train, X_test = X[:split_i], X[split_i:]
    y_train, y_test = y[:split_i], y[split_i:]

    return X_train, X_test, y_train, y_test
    

def cross_validation_split(dataset, n_folds):
    '''
    cross_validation split for np.ndarray matrix
    :param dataset: np.ndarray dataframe
    :param n_folds: k-folder cv, the number k
    :return:
    '''
    if not isinstance(dataset, np.ndarray):
        dataset = np.array(dataset)
    folder_size = dataset.shape[0] // n_folds
    for i in range(folder_size):
        pass
        # TODO finish this function
    
    