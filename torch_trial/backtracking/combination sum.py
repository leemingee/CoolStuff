'''
Created by Ming Li at 2019-02-17

Feature: 

Description: 

Contact: ming.li2@columbia.edu

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
 find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]


'''


class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        self.ans = []
        self.dfs(candidates, target, 0, [])
        return self.ans
    
    def dfs(self, candidates, target, position, curr):
        if target < 0:
            return
        elif target == 0:
            self.ans.append(curr[:])
        else:
            for i in range(position, len(candidates)):
                curr.append(candidates[i])
                self.dfs(candidates, target - candidates[i], i, curr)
                curr.pop()

class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates, res = sorted(set(candidates)), []
        stack = [(0, [], target)]
        lenth = len(candidates)
        
        while stack:
            i, temp, tar=stack.pop()
            while i<lenth and tar>0:
                if candidates[i]==tar: res+=temp+[candidates[i]],
                stack+=(i, temp+[candidates[i]], tar-candidates[i]),
                i+=1
        return res
