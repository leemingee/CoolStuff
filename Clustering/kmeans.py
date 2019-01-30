'''
Created by Ming Li at 1/17/19

Feature: np based kmeans

Description: kmeans from scratch, reduced and simpler version of sklearn

Contact: ming.li2@columbia.edu
'''

import numpy as np
import scipy
from numpy import linalg as LA

class KMeans:


    def __init__(self, k, eps):
        '''
        :param k: the number of clusters
        :param eps: The relative increment in the results before declaring convergence.
        '''
        self.k = k
        self.eps = eps
        self.centers = None

    def fit(self, D, detailed = False):
        '''
        The procedure of kmeans: (pesudocode from the link of
        https://www.researchgate.net/figure/The-pseudo-code-for-K-means-clustering-algorithm_fig2_273063437)
        input:
            k the number of clusters
            D a set of lift ratios
        output:
            k clusters
        method:
            arbitrarily choose k centers from D as initial center points
            REPEAT:
                1. reassign each element to the cluster to which the object is more similiar
                    based on the mean value of that cluster
                2. update the cluster means
            UNTIL:
                no changes for the clustering output

        :param D: input
        :param detailed: boo for print the things out or not
        :return:
        '''
        if not isinstance(D, np.ndarray):
            D = np.array(D)
        # init the centers randomly
        center_indexes = np.random.randint(D.shape[0], size=self.k)
        self.centers = D[center_indexes]
        # loop...util...
        change_flag = True
        label = None
        while change_flag:
            change_flag = False
            '''calculate the distance'''
            # refernce: https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
            dist_matrix = scipy.spatial.distance.cdist(D, self.centers)
            '''assign the cluster label'''
            label = np.argmin(dist_matrix, axis=1)
            '''reassgin the centers'''
            for i in range(self.k):
                new_center = D[label == i].mean()
                self.centers[i] = new_center
                '''change_boo judgement'''
                # np.linalg.norm() calculate the
                if LA.norm(new_center - self.centers[i]) > self.eps:
                    change_flag = True
                if detailed:
                    '''if print out the centers details'''
                    print('centers:', self.centers, 'changed:', change_flag)
        '''when jump out of the loop, print'''
        return label

    def predict(self, new_D):
        '''
        :param self:
        :param new_D: new data set for prediction
        :return: labels for prediction set
        '''
        dist_matrix = scipy.spatial.distance.cdist(new_D, self.centers)
        label = np.argmin(dist_matrix, axis=1)
        return label



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