'''
Created by Ming Li at 1/17/19

Feature: DBSCAN from scratch

Description: DBSCAN from scratch

Contact: ming.li2@columbia.edu
'''
from Cluster_min import Cluster
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy

class DBSCAN:
    '''
    DBSCAN - Density-Based Spatial Clustering of Applications with Noise.
    Finds core samples of high density and expands clusters from them.
    Good for data which contains clusters of similar density.

    reference: https://cse.buffalo.edu/~jing/cse601/fa13/materials/clustering_density.pdf
    https://github.com/SushantKafle/DBSCAN/blob/master/cluster.py
    '''
    '''
        pseudo code:
        DBSCAN(D, eps, MinPts)
             C = 0
             for each unvisited point P in dataset D
                mark P as visited
                NeighborPts = regionQuery(P, eps)
                if sizeof(NeighborPts) < MinPts
                    mark P as NOISE
                else
                    C = next cluster
                    expandCluster(P, NeighborPts, C, eps, MinPts)

        expandCluster(P, NeighborPts, C, eps, MinPts)
             add P to cluster C
             for each point P' in NeighborPts
                if P' is not visited
                    mark P' as visited
                    NeighborPts' = regionQuery(P', eps)
                    if sizeof(NeighborPts') >= MinPts
                        NeighborPts = NeighborPts joined with NeighborPts'
                if P' is not yet member of any cluster
                    add P' to cluster C

        regionQuery(P, eps)
            return all points within P's eps-neighborhood (including P)
    '''


    def __init__(self, eps, minPts, metric = 'euclidean'):
        self.eps = eps
        self.minPts = minPts
        self.metric = metric
        self.visited = []

    def fit(self, X):
        '''
        :param D: input
        :return:
        '''
        self.X = X
        self.clusters = []
        self.visited_samples = []
        self.neighbors = {}
        n_samples = np.shape(self.X)[0]
        # Iterate through samples and expand clusters from them
        # if they have more neighbors than self.min_samples
        for sample_i in range(n_samples):
            if sample_i in self.visited_samples:
                continue
            self.neighbors[sample_i] = self.__get_neighbors__(sample_i)
            if len(self.neighbors[sample_i]) >= self.minPts
                # If core point => mark as visited
                self.visited_samples.append(sample_i)
                # Sample has more neighbors than self.min_samples => expand
                # cluster from sample
                new_cluster = self.__expand_cluster__(sample_i, self.neighbors[sample_i])
                # Add cluster to list of clusters
                self.clusters.append(new_cluster)
        # Get the resulting cluster labels
        cluster_labels = self.__get_cluster_labels__()
        return cluster_labels
    
    def __get_neighbors__(self, sample_i):
        pass
    
    def __expand_cluster__(self, sample_i, neighbors_list):
        pass

    def __get_cluster_labels__(self):
        pass

# TODO read about this https://github.com/bwoneill/pypardis the dbscan on pyspark