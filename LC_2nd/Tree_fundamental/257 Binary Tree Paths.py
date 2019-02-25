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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans = []
        self.dfs(root, '')
        return self.ans
    
    def dfs(self, root, temp):
        if root:
            temp += str(root.val)
            if not root.left and not root.right:
                self.ans.append(temp)
            else:
                temp += '->'
                self.dfs(root.left, temp)
                self.dfs(root.right, temp)

class Solution2:
    #using DFS and stack to do iteratively
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []s
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path +'->'+str(node.left.val)))
            if node.right:
                stack.append((node.right, path+'->'+str(node.right.val)))
        return paths

if __name__ == '__main__':
    res = Solution()
    print(res)