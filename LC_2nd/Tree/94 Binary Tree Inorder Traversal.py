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
    
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        '''inorder traversal using recursion'''
        self.ans = []
        self.helper(root, self.ans)
        return self.ans
    
    def helper(self, root, res):
        if root is not None:
            if root.left is not None:
                self.helper(root.left, res)
            res.append(root.val)
            if root.right is not None:
                self.helper(root.right, res)
                
class Solution2:
    # this is using the iterative
    def inorderTraversal(self, root):
        curr = root
        stack = []
        res = []
        
        while curr is not None or len(stack) != 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

#TODO the morris method: Approach 3: Morris Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/solution/

if __name__ == '__main__':
    res = Solution()
    print(res)