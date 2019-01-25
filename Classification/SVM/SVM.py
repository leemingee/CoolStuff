'''
Created by Ming Li at 2019-01-24

Feature: SVM

Description: SVM using SMO algorithm

Contact: ming.li2@columbia.edu
'''

import numpy as np
np.set_printoptions(precision=4)

class SVM:
    
    def __init__(self):
        self.alpha = None
        self.b = 0
        self.kernel = None
        self.x = None
        self.y = None
    
    def fit(self, X, y):
        # fit method is the main part we need to solve
        # using opt techs to update self.b, self.w
        # reference: https://pythonprogramming.net/svm-optimization-python-machine-
        # \learning-tutorial/?completed=/svm-in-python-machine-learning-tutorial/
        pass
    
    def predict(self, X_test):
        '''
        the predict process of SVM, here, we solve it by the traditional formula
        y_pred = sign(w * x + b)
        :param X_test:
        :return:
        '''
        y_pred = np.sign(np.dot(np.array(features), self.w) + self.b)
        return y_pred