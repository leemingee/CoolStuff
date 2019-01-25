'''
Created by Ming Li at 2019-01-24

Feature: SVM

Description: SVM using SMO algorithm

Contact: ming.li2@columbia.edu
'''

import numpy as np
np.set_printoptions(precision=4)

# constant for simulation here
data_dict = {-1: np.array([[1, 7],
                           [2, 8],
                           [3, 8], ]),

             1: np.array([[5, 1],
                          [6, -1],
                          [7, 3], ])}

class SVM:
    
    def __init__(self):
        self.alpha = None
        self.b = 0
        self.kernel = None
        self.x = None
        self.y = None
    
    def fit(self, data):
        # fit method is the main part we need to solve
        # using opt techs to update self.b, self.w
        # reference: https://pythonprogramming.net/svm-optimization-python-machine-
        # \learning-tutorial/?completed=/svm-in-python-machine-learning-tutorial/
        #TODO try using np to solve the opt problem
        self.data = data
        opt_dict = {}

        transforms = [[1, 1],
                      [-1, 1],
                      [-1, -1],
                      [1, -1]]
        #todo not sure about what the transform needs to be
        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None # delete the all_data once we got the feature of max_all_data and min_all_data

        # we get several step size to make sure the learning rate is adjusted by hardcode
        step_sizes = [self.max_feature_value * 0.1,
                      self.max_feature_value * 0.01,
                      # starts getting very high cost after this.
                      self.max_feature_value * 0.001]

        # extremely expensive
        b_range_multiple = 5
        b_multiple = 5
        latest_optimum = self.max_feature_value * 10

        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum])
            # we can do this because convex
            optimized = False
            while not optimized:
                pass
        
        #TODO try using libsvm for solving the opt problem
    
    def predict(self, X_test):
        '''
        the predict process of SVM, here, we solve it by the traditional formula
        y_pred = sign(w * x + b)
        :param X_test:
        :return:
        '''
        y_pred = np.sign(np.dot(np.array(features), self.w) + self.b)
        return y_pred