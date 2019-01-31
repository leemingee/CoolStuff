'''
Created by Ming Li at 2019-01-31

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
import numpy as np
import numpy.linalg as LA
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

        self.responsibilities = []
        self.responsibility = None
        
    
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
            self.parameters.append(param_each)
        # initial the prior weights
        self.priors = (1 / self.k) * np.ones(self.k)
        
    def __likelihood_for_Gaussian__(self, X, params_each):
        '''
        calculate the likelihood pairs for each data point for one specific gaussian distribution
        :param X: dataset
        :param params: params
        :return:
        '''
        n_features = X.shape[1]
        mean = params_each['mean']
        cov = params_each['cov']
        assert mean != None, 'mean should not be None, check the input dic'
        assert cov != None, 'cov should not be None, check the input dic'

        determinant = np.linalg.det(cov)
        likelihoods = np.zeros(shape=(X.shape[0]))
        
        for i, each_datapoint in enumerate(X):
            d = n_features # dimension
            # coeff for multi gaussian
            coeff = 1.0 * np.sqrt(determinant) / np.power((2 * np.pi), d/2)
            exponent = np.exp(-0.5 * (each_datapoint - mean).T.dot(np.linalg.pinv(cov)).dot((each_datapoint - mean)))
            likelihoods[i] = coeff * exponent
        return likelihoods
    
    def __likelihoods_for_Multi_Gaussian__(self, X):
        likelihoods = np.zeros(shape=(X.shape[0], self.k))
        for each_gaussian in self.k:
            likelihoods[:, each_gaussian] = self.__likelihood_for_Gaussian__(X, self.parameters[each_gaussian])
        return likelihoods
    
    def expectation(self, X):
        '''calculate the prob for each datapoint-gaussian pairs'''
        weighted_likelihoods = self.__likelihoods_for_Multi_Gaussian__(X) * self.priors
        sum_likelihoods = np.expand_dims(np.sum(weighted_likelihoods, axis=1), axis=1)
        # Determine responsibility as P(X|y)*P(y)/P(X)
        self.responsibility = weighted_likelihoods / sum_likelihoods
        # Assign samples to cluster that has largest probability
        self.sample_assignments = self.responsibility.argmax(axis=1)
        # Save value for convergence check
        self.responsibilities.append(np.max(self.responsibility, axis=1))
        #TODO make it more detailed and figure it out

    def maximization(self, X):
        """ Update the parameters and priors """
        # Iterate through clusters and recalculate mean and covariance
        for i in range(self.k):
            resp = np.expand_dims(self.responsibility[:, i], axis=1)
            mean = (resp * X).sum(axis=0) / resp.sum()
            covariance = (X - mean).T.dot((X - mean) * resp) / resp.sum()
            self.parameters[i]["mean"], self.parameters[
                i]["cov"] = mean, covariance
    
        # Update weights
        n_samples = np.shape(X)[0]
        self.priors = self.responsibility.sum(axis=0) / n_samples

    def __converge_judge__(self, X):
        """ Covergence if || likehood - last_likelihood || < tolerance """
        if len(self.responsibilities) < 2:
            return False
        diff = np.linalg.norm(
            self.responsibilities[-1] - self.responsibilities[-2])
        # print ("Likelihood update: %s (tol: %s)" % (diff, self.tolerance))
        return diff <= self.tolerance

    def predict(self, X):
        """ Run GMM and return the cluster indices """
        # Initialize the gaussians randomly
        self.__init_Gaussian_param_randomly__(X)
    
        # Run EM until convergence or for max iterations
        for _ in range(self.max_iterations):
            self.expectation(X)  # E-step
            self.maximization(X)  # M-step
        
            # Check convergence
            if self.__converge_judge__(X):
                break
    
        # Make new assignments and return them
        self.expectation(X)
        return self.sample_assignments
        
            
        