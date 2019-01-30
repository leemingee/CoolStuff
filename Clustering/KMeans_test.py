'''
Created by Ming Li at 2019-01-30

Feature: kmeans with unit test

Description: kmeans module with test

Contact: ming.li2@columbia.edu

key expression:

from scipy.spatial import distance
dist_matrix = distance.cdist(x, self.centers)
labels = np.argmin(dist_matrix, axis=1)

from numpy import linalg as LA
if LA.norm(new_center-self.centers[cluster] > self.eps:
    stopped = False

'''

import numpy as np
from numpy import linalg as LA
import scipy
from scipy.spatial import distance

class KMeans:
    
    def __init__(self, k, eps):
        '''
        init a Kmeans cluster
        :param k: number of clusters
        :param eps: convergence limit
        '''
        self.k = k
        self.eps = eps
    
    
    def fit(self, x, detailed = False):
        '''
        fit for dataset x
        :param x: dataset input, should be np.ndarray
        :param detailed: boolean for print out or not
        :return: the label of each x
        '''
        '''
        algorithm overview:
        1. assigned the k centers randomly
        2.1 assigned the other points to cluster which has the minimum distance
        2.2 calculate the centers again by using the center of each clusters
        3. loop till changes less than eps
        '''
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        n_samples = x.shape[0]
        '''assign the k centers randomly'''
        centers_idx = np.random.randint(n_samples, size=self.k)
        self.centers = x[centers_idx]
        '''step 2, loop till part'''
        stopped = False
        label = None
        while not stopped:
            stopped = True
            '''2.1 calculate the distance pairs'''
            distances_matrix = distance.cdist(x, self.centers) # shape of a, shape of b
            '''2.1 assign the labels'''
            label = np.argmin(distances_matrix, axis=1)
            '''2.2 assign new centers'''
            for cluster in range(self.k):
                k_cluster_idx = label == cluster
                new_center = np.mean(x[k_cluster_idx])
                if LA.norm(self.centers[cluster] - new_center) > self.eps:
                    stopped = False
                self.centers[cluster] = new_center
            if detailed == True:
                print('centers are {}'.format(self.centers))
        return label
    
    def predict(self, x_new):
        '''
        predict module for kmeans, used for predict the cluster label for new x_new
        :param x_new: new data point
        :return: the label
        '''
        assert x_new.shape[1] == self.centers.shape[1], 'the dim of x_new should be the same as x/centers, centers dim: {}'.format(self.centers.shape[1])
        distance_matrix = distance.cdist(x_new, self.centers)
        predicted = np.argmin(distance_matrix, axis=1)
        return predicted
                
            

class test:
    
    def __init__(self):
        pass
    '''only used for test for some module'''
    def test_scipy(self):
        '''test for scipy distance module'''
        print(scipy.__version__)
        from scipy.spatial import distance
        a = np.array([[0, 0, 0],
                      [0, 0, 1],
                      [0, 1, 0],
                      [0, 1, 1],
                      [1, 0, 0],
                      [1, 0, 1],
                      [1, 1, 0],
                      [1, 1, 1]])
        b = np.array([[0, 0, 0],
                      [0, 0, 1],
                      [0, 1, 0],
                      [0, 1, 1]])
        print(distance.cdist(a, b))
        print(np.argmin(distance.cdist(a, b), axis=1)) # [0 1 2 3 0 1 2 3]
        print(np.argmin(distance.cdist(a, b), axis=0)) # [0 1 2 3]
        print(distance.cdist(a, b).shape) # shape of a, shape of b
    
    def test_fit(self, x, k, eps):
        '''test for predict module'''
        kmeans = KMeans(k, eps)
        labels = kmeans.fit(x)
        print(labels)
    
    def test_predict(self, x, k, eps, x_new):
        kmeans = KMeans(k, eps)
        _ = kmeans.fit(x)
        predicted = kmeans.predict(x_new)
        print(predicted)
        
    
    

def main():
    np.random.seed(3)
    unit_test = test()
    x = np.random.randn(20, 4)
    k, eps = 3, 1e-2
    unit_test.test_fit(x, k, eps)
    x_new = np.random.randn(5, 4)
    x_new2 = np.random.randn(10, 3)
    try:
        unit_test.test_predict(x, k, eps, x_new2)
    except Exception as e:
        print(e)
    unit_test.test_predict(x, k, eps, x_new)
    
    
if __name__ == "__main__":
    main()
    