'''
Created by Ming Li at 2019-01-24

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
import numpy as np

def euclidean_distance(x1, x2):
    """ Calculates the l2 distance between two vectors """
    distance = 0
    # Squared distance between each coordinate
    for i in range(len(x1)):
        distance += pow((x1[i] - x2[i]), 2)
    return math.sqrt(distance)

class KNN:
    
    def __init__(self, k = 5):
        self.k = k
        
    def __vote__(self, neighbor_labels):
        labels, counts = np.unique(neighbor_labels, return_counts=True)
        idx = np.argmax(counts)
        return labels[idx]
    
    def predict(self, X_test, X_train, y_train):
        y_pred = np.zeros(X_test.shape[0])
        for idx, test_elem in enumerate(X_test):
            # get the distance pair between test_elem and train_elem and sort them, get the idx of closet k train_elem
            # TODO this distance_pairs can be stored using tree based algorithms
            # TODO this 
            distance_pairs = [euclidean_distance(test_elem, train_elem) for train_elem in X_train]
            first_k_idx = np.argsort(distance_pairs)[: self.k]
            k_neighbor_labels = y_train[first_k_idx]
            y_pred[idx] = self.__vote__(neighbor_labels=k_neighbor_labels)
        return y_pred