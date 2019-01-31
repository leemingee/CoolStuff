'''
Created by Ming Li at 1/17/19

Feature: logistic regression

Description: logistics regression
the code is from reference link
https://medium.com/@martinpella/logistic-regression-from-scratch-in-python-124c5636b8ac

Contact: ming.li2@columbia.edu
'''
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class LR:
    
    def __init__(self, num_iters, lr=0.1, fit_intercept = True, verbose = True, regularization = 'l2'):
        self.num_iters = num_iters
        self.fit_intercept = fit_intercept
        self.verbose = verbose
        self.lr = lr
        self.regularization = regularization
    
    def __sigmoid__(self, z):
        return 1.0 / (1 + np.exp(-z))
    
    def __add_intercept__(self, X):
        intercept = np.ones((X.shape[0], 1))
        X = np.concatenate((intercept, X), axis = 1)
        return X
    
    def loss(self, h, y):
        '''here returns the negative log loss term'''
        loss_term = ( - y.T.dot(np.log(h)) - (1 - y).T.dot(np.log(1-h)) ).mean()
        return loss_term
    
    def fit(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept__(X) # X.shape (100, 3)
        # initial the theta
        self.theta = np.zeros(X.shape[1])
        for iter in range(self.num_iters):
            '''for every iteration, calculate the gradient and update the theta'''
            h = self.__sigmoid__(np.dot(X, self.theta)) # h.shape (100,) self.theta.shape (3,)
            gradient = np.dot( X.T, (h - y) ) / len(y) # gradient.shape (3,)
            # update the theta
            self.theta -= self.lr * gradient
            
            if self.verbose and iter % 1000 == 0:
                # print('{} iterations: loss = {0:.2f}'.format(iter, self.loss(h, y)))
                print('{} iterations: loss = {}'.format(iter, self.loss(h, y)))
    
    def predict_proba(self, X_new):
        if self.fit_intercept:
            X_new = self.__add_intercept__(X_new)
        return self.__sigmoid__(np.dot(X_new, self.theta))
    
    def predict(self, X_new, threshold = 0.5):
        return self.predict_proba(X_new) >= threshold

def main():
    lr = LR(10000)
    iris = load_iris()
    X = iris.data[:, :2]
    y = (iris.target != 0) * 1
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
    lr.fit(X_train, y_train)
    preds = lr.predict(X_test)
    print('acc {}'.format(accuracy_score(y_pred=preds, y_true=y_test)))

if __name__ == '__main__':
    main()
    
    
# TODO: the initial cluster centers using kmeans++
'''
    Selects initial cluster centers for k-mean clustering in a smart way
    to speed up convergence. see: Arthur, D. and Vassilvitskii, S.
    "k-means++: the advantages of careful seeding". ACM-SIAM symposium
    on Discrete algorithms. 2007
    Version ported from http://www.stanford.edu/~darthur/kMeansppTest.zip,
    which is the implementation used in the aforementioned paper.
'''

# TODO add parallel module and give it a try

# TODO minibatch kmeans to be implemented