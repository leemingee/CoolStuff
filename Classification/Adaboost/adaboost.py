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

class TrivialClassification:
    def __init__(self):
        self.sign = None
        self.thres = 0
    
    def __str__(self):
        return self.sign + " than " + str(self.thres)
    
    def fit(self, x, y, w=None):
        if w is None:
            w = np.ones(len(y)) / len(y)
        data = zip(x, y, w)
        data = sorted(data, key=lambda s: s[0])
        [x, y, w] = zip(*data)
        y = np.array(y)
        w = np.array(w)
        correct = np.zeros((2, len(y)))  # 0 row for x < v, 1 row for x >= v
        for i in range(len(y)):
            w_front = w[:i]
            w_back = w[i:]
            correct[0, i] += np.sum(w_front[y[:i] == 1]) + np.sum(w_back[y[i:] == -1])
            correct[1, i] += np.sum(w_front[y[:i] == -1]) + np.sum(w_back[y[i:] == 1])
        idx = np.argmax(correct, axis=1)
        if correct[0, int(idx[0])] > correct[1, int(idx[1])]:
            self.sign = "smaller"
            self.thres = x[idx[0]]
        else:
            self.sign = "equal to or bigger"
            self.thres = x[idx[1]]
    
    def predict(self, x):
        if self.sign == "smaller":
            return (x < self.thres) * 2 - 1
        else:
            return (x >= self.thres) * 2 - 1
    
    def score(self, x, y, w=None):  # the wrong percent
        if w is None:
            w = np.ones(len(y)) / len(y)
        return 1 - np.sum(w[self.predict(x) == y])

class weak_learner_unit:
    
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
        # self.weights = []
    
    @staticmethod
    def __calcAlpha__(self, err):
        return 0.5 * np.log((1 - err) / err)
    
    def fit(self, X, y, verbose = False):
        weights = np.ones(len(y)) / len(y) # initial the weights for each data sample
        accuracy = 0
        epoch = 0
        while 1 - accuracy > self.epsilon or epoch <= self.iters:
            # stop when acc is okay or epoch number is larger than iters
            epoch += 1
            weak_learner = weak_learner_unit()
            alpha = AdaBoost.calcAlpha(weak_learner.score(X, y, weights))
            self.alphas.append(alpha)
            self.weak_learners_list.append(weak_learner)
            # update the weights by w :=
            weights = weights * np.exp(-alpha * y * self.predict(X))
            weights = weights / np.sum(weights)
            accuracy = self.accuracy(X, y)
            
            
    
    def predict(self, X_new):
        len_X_new = X_new.shape[0]
        predicted = [0] * len_X_new
        for idx in range(len(self.weak_learners_list)):
            predicted += self.weak_learner_list[idx].predict(X_new) * self.alphas[idx]
        return (predicted > 0) * 2 - 1
        
    def accuracy(self, x, y):
        acc = np.sum(self.predict(x) == y) / len(y)
        return acc

