'''
Created by Ming Li at 2019-02-24

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        children = root.children
        
        if not any(children):
            return 1
        max_depth = float('-inf')
        for c in children:
            max_depth = max(max_depth, self.maxDepth(c))
        return max_depth + 1



if __name__ == '__main__':
    res = Solution()
    print(res)