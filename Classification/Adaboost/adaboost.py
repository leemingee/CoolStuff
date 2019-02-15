'''
Created by Ming Li at 2019-02-13

Feature: adaboost

Description: adaboost, the base_esimator is decision tree where depth = 1

Reference link:
https://anujkatiyal.com/blog/2017/10/24/ml-adaboost/#.XGT0jM9KjdQ for the overall structure of the code

Contact: ming.li2@columbia.edu
'''
from numpy import np

# todo using subclass from some existing class, like decisiontree classifier to accomplish for the weak-learner part
# reference link:
# https://www.cnblogs.com/bigberg/p/7182741.html
# https://www.cnblogs.com/feeland/p/4419121.html

class weak_learner:
    
    def __init__(self):
        pass
    
    def predict(self, X_new):
        pass
    
    def fit(self, X, y):
        pass
    

class Adaboost:
    
    def __init__(self, weak_learner_class, epsilon = 0.1, iters = 100):
        self.weak_learner_class = weak_learner_class
        self.epsilon = epsilon
        self.alphas = []
        self.weak_learners_list = []
        self.iters = iters
    
    def __calcAlpha__(self, e):
        return 0.5 * np.log( (1-e)/e )
    
    def fit(self, X, y, verbose = False):
        pass
    
    def predict(self, X_new):
        len_X_new = X_new.shape[0]
        predicted = [0] * len_X_new
        for idx in range(len(self.weak_learners_list)):
            predicted += self.weak_learner_list[idx].predict(X_new) * self.alphas[idx]
        return (predicted > 0) * 2 - 1
        
    def accuracy(self, x, y):
        acc = np.sum(self.predict(x) == y) / len(y)
        return acc
