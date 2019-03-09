import time
import numpy as np

def pca_naive(X, K):
    """
    PCA -- naive version

    Inputs:
    - X: (float) A numpy array of shape (N, D) where N is the number of samples,
         D is the number of features
    - K: (int) indicates the number of features you are going to keep after
         dimensionality reduction

    Returns a tuple of:
    - P: (float) A numpy array of shape (K, D), representing the top K
         principal components
    - T: (float) A numpy vector of length K, showing the score of each
         component vector
    """

    ###############################################
    #TODO: Implement PCA by extracting eigenvector#
    #You may need to sort the eigenvalues to get  #
    #             the top K of them.              #
    ###############################################
    X -= X.mean(axis=0)
    R = np.cov(X.T)
    eigenvalues, eigenvector = np.linalg.eig(R)
    P = eigenvector[:K]
    T = eigenvalues/sum(eigenvalues)
    T = T[:K]

    ###############################################
    #              End of your code               #
    ###############################################
    
    return (P, T)
