'''
Created by Ming Li at 2019-02-18

Feature: 

Description: PCA using np

Contact: ming.li2@columbia.edu
'''

import numpy as np
import numpy.linalg as LA

class PCA:
    def __init__(self):
        pass

    def fit(self, x, dim=2):
        e_val, e_vec = LA.eig(np.cov(x, rowvar=False))
        idx = e_val.argsort()[::-1]
        e_vec = e_vec[:, idx][:, :dim]
        return x.dot(e_vec)
