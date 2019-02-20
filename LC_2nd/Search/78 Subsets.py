'''
Created by Ming Li at 2019-02-20

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        self.ans = []
        for n in range(len(nums) + 1):
            self.backtracking(nums, n, 0, [])
        return self.ans
    
    def backtracking(self, nums, n, start, temp):
        if len(temp) == n:
            self.ans.append(temp[:])
            return
        for i in range(start, len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.backtracking(nums, n, i, temp)
            temp.pop()


if __name__ == '__main__':
    res = Solution()
    print(res)