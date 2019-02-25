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
    # using recursion
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        children = [root.left, root.right]
        # if we're at leaf node
        if not any(children):
            return 1
        
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1


class Solution2:
    # using DFS and stack to do it iteratively
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root), ], float('inf')
        
        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))
        return min_depth

    def minDepth(self, root):
        from collections import deque
        if not root:
            return 0
        else:
            node_queue = deque([(1, root), ])


class Solution3:
    
    def minDepth(self, root):
        # using BFS
        from collections import deque
        if not root:
            return 0
        else:
            node_queue = deque([(1, root), ])
        
        while node_queue:
            depth, root = node_queue.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_queue.append((depth + 1, c))


if __name__ == '__main__':
    res = Solution()
    print(res)