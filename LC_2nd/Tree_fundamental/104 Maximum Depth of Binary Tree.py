'''
Created by Ming Li at 2019-02-24

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            if not root.left and not root.right:
                return 1
            else:
                return 1 + max(self.maxDepth(root.left),
                              self.maxDepth(root.right))

if __name__ == '__main__':
    res = Solution()
    print(res)