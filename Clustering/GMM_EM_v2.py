'''
Created by Ming Li at 2019-01-31

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
import numpy as np
from utils_GMM_EM_v2 import normalize, euclidean_distance, calculate_covariance_matrix


class GMM:
    """
    A probabilistic clustering method for determining groupings among data samples.
    Parameters:
    -----------
    k: int
        The number of clusters the algorithm will form.
    max_iterations: int
        The number of iterations the algorithm will run for if it does
        not converge before that.
    tolerance: float
        If the difference of the results from one iteration to the next is
        smaller than this value we will say that the algorithm has converged.
    """
    
    def __init__(self, k=2, max_iterations=2000, tolerance=1e-8):
        self.k = k
        self.max_iterations = 2000
        self.tolerance = tolerance
        # initial the params
        self.parameters = []
        # initial the assignment
        self.sample_assignments = None
        
    
    def __init_Gaussian_param_randomly__(self, X):
        '''
        initial the params for each gaussian distribution
        :param X:
        :return: update the self.parameters list
        '''
        n_samples = X.shape[0]
        for each_gaussian in self.k:
            param_each = {}
            param_each['mean'] = X[np.random.choice(range(n_samples))]
            param_each['cov'] = calculate_covariance_matrix(X)