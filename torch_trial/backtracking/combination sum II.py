'''
Created by Ming Li at 2019-02-17

Feature: 

Description: 

Contact: ming.li2@columbia.edu


Given a collection of candidate numbers (candidates) and a target number (target), find all unique
combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = 
[10,1,2,7,6,1,5]
, target = 
8
,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

'''


class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        self.ans = []
        self.used = [False] * len(candidates)
        self.dfs(sorted(candidates), target, 0, [])
        return self.ans
    
    def dfs(self, candidates, target, position, curr):
        if target < 0:
            return
        elif target == 0:
            self.ans.append(curr[:])
        else:
            for i in range(position, len(candidates)):
                if i > position and candidates[i] == candidates[i - 1]:
                # [NOTE] difference, start from position, if the following next is the same, then jump next loop
                    continue
                curr.append(candidates[i])
                self.dfs(candidates, target - candidates[i], i + 1, curr)
                # [NOTE] difference, from i to i + 1, start from the next number
                curr.pop()