'''
Created by Ming Li at 1/17/19

Feature: DBSCAN from scratch

Description: DBSCAN from scratch

Contact: ming.li2@columbia.edu
'''

class DBSCAN:
    '''
    DBSCAN - Density-Based Spatial Clustering of Applications with Noise.
    Finds core samples of high density and expands clusters from them.
    Good for data which contains clusters of similar density.

    reference: https://cse.buffalo.edu/~jing/cse601/fa13/materials/clustering_density.pdf
    '''

    def __init__(self, eps, minPts, metric = 'euclidean'):
        self.eps = eps
        self.minPts = minPts
        self.metric = metric
        self.visited = []

    def fit(self, D):
        '''
        :param D: input
        :return:
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


# TODO read about this https://github.com/bwoneill/pypardis the dbscan on pyspark