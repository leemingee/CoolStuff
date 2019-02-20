'''
Created by Ming Li at 2019-02-20

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''

class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        p = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = p * res[i]
            p *= nums[i]
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = p * res[i]
            p *= nums[i]
        
        return res

if __name__ == '__main__':
    res = Solution()
    print(res)