'''
Created by Ming Li at 1/17/19

Feature: the minimum cluster class

Description: some helper functions for clustering

Contact: ming.li2@columbia.edu
'''
import numpy as np

class Cluster(object):
    def __init__(self, name, dim):
        self.name = name
        self.dim = dim
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def get_points(self):
        return self.points

    def erase(self):
        self.points = []

    def has(self, point):
        return point in self.points

    def __str__(self):
        return "%s: %d points" % (self.name, len(self.points))