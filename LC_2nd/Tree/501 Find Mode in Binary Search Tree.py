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
    # O(1) space
    # TODO read this long solution
    def findMode(self, root):
        if root is None: return []
        
        self.max_mode = 1
        self.cur_mode = 1
        self.max_modes = set([root.val])
        self.prev_node = None
        
        self.find_mode_inorder(root)
        
        return list(self.max_modes)
    
    def find_mode_inorder(self, root):
        if root is None: return
        
        self.find_mode_inorder(root.left)
        
        self.update_modes(root)
        self.prev_node = root
        
        self.find_mode_inorder(root.right)
    
    def update_modes(self, root):
        if self.prev_node is not None and self.prev_node.val == root.val:
            self.cur_mode += 1
            if self.cur_mode >= self.max_mode:
                if self.cur_mode > self.max_mode: self.max_modes.clear()
                self.max_modes.add(root.val)
                self.max_mode = self.cur_mode
        else:
            self.cur_mode = 1
            if self.max_mode == self.cur_mode: self.max_modes.add(root.val)

class Solution2:
    # not O(1) space, O(n) time, O(n) space
    def findMode(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        # using any traversal and then counter it
        self.traversal = {}
        self.helper(root)
        max_ct = max(self.traversal.values())
        # [(v, k) for (k, v) in d.items()]
        return [k for (k, v) in self.traversal.items() if v == max_ct]
    
    def helper(self, root):
        # inorder traversal staff
        if root is not None:
            if root.left is not None:
                self.helper(root.left)
            if root.val not in self.traversal:
                self.traversal[root.val] = 1
            else:
                self.traversal[root.val] = 1 + self.traversal[root.val]
            if root.right is not None:
                self.helper(root.right)



if __name__ == '__main__':
    res = Solution()
    print(res)