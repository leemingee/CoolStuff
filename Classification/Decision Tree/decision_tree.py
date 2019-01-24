'''
Created by Ming Li at 2019-01-23

Feature: Decision Tree classifier

Description: Decicion Tree Classifier from scratch

Contact: ming.li2@columbia.edu
'''
import numpy as np
from utils_decision_tree import *


class Node:
    def __init__(self, key, val, depth):
        '''
        :param key:
        :param val:
        :param depth:
        '''
        self.val = val
        self.key = key
        self.depth = depth
        self.children = []
        
    def __str__(self):
        '''
        function to print the node information
        :return: the node information
        [TODO] change the print to formatted string
        '''
        ans = "{NODE_KEY}: {NODE_VAL} ({NODE_CHILD})"
        if not self.children:
            ans = ans.format(NODE_KEY=self.key, NODE_VAL=self.val, NODE_CHILD = "None")
        else:
            node_child = ""
            for child in self.children:
                node_child += str(child) + ", "
            ans = ans.format(NODE_KEY=self.key, NODE_VAL=self.val, NODE_CHILD = "None")
        return ans
    
    
    def add_child(self, key, val, depth = 0):
        self.children.append(Node(key, val, depth))
        return self.children[-1]

class DecisionTree:
    #TODO add decorator and unit test
    def __init__(self, epsilon = 0, max_depth = -1):
        '''
        here depth=-1 means no constrain
        :param epsilon:
        :param max_depth:
        '''
        self.root = Node("root", 0, max_depth)
        self.epsilon = epsilon
        self.type = None
        
    
    def fit(self, x, y, type = 'CART', detailed = False):
        self.type = type
        if type == 'CART':
            self.CARTGenerator(x, y, self.root, detailed)
        else:
            self.generate(x, y, self.root, type, detailed)
            
    
    def generate(self, x, y, type, detailed):
        pass
    
    def CARTGenerator(self, x, y, detailed):
        pass
    
    def predict(self, x):
        pass
    
    def pruning(self, root):
        pass
    

        
        
    
