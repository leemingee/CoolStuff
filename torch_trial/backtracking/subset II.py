'''
Created by Ming Li at 2019-02-17

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        # method 2: the dfs and backtracking
        nums = sorted(nums)
        self.ans = []
        for i in range(len(nums) + 1):
            self.backtracking(nums, i, 0, [])
        return self.ans
    
    def backtracking(self, nums, length, start, cur):
        if len(cur) == length:
            self.ans.append(cur[:])
            return
        for i in range(start, len(nums)):
            if i > start and nums[i - 1] == nums[i]:
                continue
            cur.append(nums[i])
            self.backtracking(nums, length, i + 1, cur)
            cur.pop()