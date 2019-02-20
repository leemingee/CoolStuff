'''
Created by Ming Li at 2019-02-20

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
    def isValidBST2(self, root: 'TreeNode') -> 'bool':
        # the inorder traversal of BST is a ascending list
        stack = []
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True

    def isValidBST(self, root: 'TreeNode') -> 'bool':
        # solution using the recursion
        return self.validhelper(root, float('-inf'), float('inf'))

    def validhelper(self, root, min_val, max_val):
        if root is None:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        else:
            result = self.validhelper(root.left, min_val, root.val) and self.validhelper(root.right, root.val,
                                                                                         max_val)
            return result


if __name__ == '__main__':
    res = Solution()
    print(res)