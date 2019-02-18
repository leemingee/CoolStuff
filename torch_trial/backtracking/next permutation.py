'''
Created by Ming Li at 2019-02-17

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                for j in range(len(nums) - 1, 0, -1):
                    if nums[j] > nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        break
                break
            i -= 1
        nums[i:] = nums[i:][::-1]