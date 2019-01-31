'''
Created by Ming Li at 2019-01-30

Feature: 

Description: logistic regression with l2 norm regularization term
            The optimizaation part is realized by the scipy.optimize module,
            using minimum API for some function regarding to some variable

Reference link:
https://www.kaggle.com/anthonysegura/logistic-regression-from-scratch

Contact: ming.li2@columbia.edu
'''
import numpy as np
import scipy as sp
from scipy import optimize as op

def sigmoid(score):
    return 1.0 / (1 + np.exp(-score))

def loss_function_with_reg(theta, X, y, _lambda = 0.1):
    '''
    loss function for logistic regression with l2 norm regularization term
    :param theta: the params for logistics regression
    :param X: input X
    :param y: input y
    :return: the logistic regression loss given coefficients and input data
    '''
    assert X.shape[0] == len(y), 'X y should have the same dimension!'
    if not isinstance(X, np.ndarray):
        X = np.array(X)
    m = len(y)
    h = sigmoid(X.dot(theta))
    regular_term = 0.5 * _lambda * np.sum(theta ** 2) / m
    loss = 1.0/m * ( -y.T.dot(np.log(h)) - (1-y).T.dot(np.log(1-h)) ) + regular_term
    return loss

def gradient_with_reg(theta, X, y, _lambda = 0.1):
    m, n = X.shape
    theta = theta.reshape((n, 1))
    y = y.reshape((m, 1))
    h = sigmoid(X.dot(theta))
    reg = _lambda * theta / m
    gradient = 1.0 * X.T.dot(h - y) / m + reg
    return gradient


def logisticRegression(X, y, theta):
    result = op.minimize(fun=loss_function_with_reg, x0=theta, args=(X, y),
                         method='TNC', jac=gradient_with_reg)
    
    return result.x