'''
Created by Ming Li at 2019-02-19

Feature: 

Description: https://leetcode.com/problems/permutations-ii/

Contact: ming.li2@columbia.edu
'''


class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        self.ans = []
        self.used = [False] * len(nums)
        self.backtracking(sorted(nums), len(nums), [])
        return self.ans
    
    def backtracking(self, nums, n, temp):
        if len(temp) == n:
            self.ans.append(temp[:])
        for i in range(len(nums)):
            if self.used[i] == True:
                continue
            if i > 0 and self.used[i - 1] == True and nums[i] == nums[i - 1]:
                continue
            self.used[i] = True
            temp.append(nums[i])
            self.backtracking(nums, n, temp)
            temp.pop()
            self.used[i] = False


if __name__ == '__main__':
    res = Solution().permuteUnique([1,1,2,1])
    print(res)