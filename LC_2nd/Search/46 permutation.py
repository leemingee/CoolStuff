'''
Created by Ming Li at 2019-02-19

Feature: 

Description: https://leetcode.com/problems/permutations/

Contact: ming.li2@columbia.edu
'''


class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        # corner cases check
        if len(nums) == 0:
            return []
        else:
            self.ans = []
            self.visited = [False] * len(nums)
            self.backtracking(nums, len(nums), [])
            return self.ans
    
    def backtracking(self, nums, n, temp):
        if n == len(temp):
            self.ans.append(temp[:])
        for i in range(len(nums)):
            if self.visited[i] == True:
                continue
            self.visited[i] = True
            temp.append(nums[i])
            self.backtracking(nums, n, temp)
            temp.pop()
            self.visited[i] = False


if __name__ == '__main__':
    res = Solution().permute([1, 2, 3])
    print(res)