# Created by Ming Li at 3/7/2019

# Feature: 

# Description:

# Contact: ming.li2@columbia.edu
import numpy as np

class loss:

    def __init__(self, x, y):
        """
        Inputs:
        - X: (float) a tensor of shape (N, #classes)
        - y: (int) ground truth label, a array of length N
        """
        self.x = x
        self.y = y

    def softmax_loss(self):
        # initial
        loss = 0.0
        dx = np.zeros_like(self.x)
        # calculate the loss
        p = np.exp(self.x - np.max(self.x, axis=1, keepdims=True))
        p /= np.sum(p, axis=1, keepdims=True)
        num_train = self.x.shape[0]
        loss = -np.sum(np.log(p[np.arange(num_train), self.y]))
        loss /= num_train
        dx = p.copy()
        dx[np.arange(num_train), self.y] -= 1
        dx /= num_train
        return loss, dx