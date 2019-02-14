'''
Created by Ming Li at 2019-02-13

Feature: adaboost

Description: adaboost, the base_esimator is decision tree where depth = 1

Reference link:
https://anujkatiyal.com/blog/2017/10/24/ml-adaboost/#.XGT0jM9KjdQ for the overall structure of the code

Contact: ming.li2@columbia.edu
'''
from numpy import np

class weak_learner:
    
    def __init__(self):
        pass
    
    def predict(self, X_new):
        pass
    
    def fit(self, X, y):
        pass
    

class Adaboost:
    
    def __init__(self, weak_learner_class, epsilon = 0.1):
        self.weak_learner_class = weak_learner_class
        self.epsilon = epsilon
        self.alphas = []
        self.weak_learners_list = []
    
    def __calcAlpha__(self, e):
        return 0.5 * np.log( (1-e)/e )
    
    def fit(self, X, y, verbose = False):
        pass
    
    def predict(self, X_new):
        pass
    
    def score(self, x, y):
        pass
