'''
Created by Ming Li at 2019-02-17

Feature: 

Description: 

Contact: ming.li2@columbia.edu

Find all possible combinations of k numbers that add up to a number n, given that only numbers from
1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

'''


class Solution:
    def combinationSum3(self, k: 'int', n: 'int') -> 'List[List[int]]':
        self.ans = []
        candidates = list(range(1, 10))
        self.dfs(candidates, k, n, [])
        return self.ans
    
    def dfs(self, candidates, k, target, curr):
        if target < 0 or k < 0:
            return
        if target > 0 and k == 0:
            return
        if target == 0 and k == 0:
            self.ans.append(curr[:])
        for i in range(len(candidates)):
            curr.append(candidates[i])
            self.dfs(candidates[i + 1:], k - 1, target - candidates[i], curr)
            curr.pop()
