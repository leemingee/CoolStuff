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


def main():
    n = Node(1, 1, 1)
    ans = n.__str__()
    print(ans)


if __name__ == '__main__':
    main()
    
