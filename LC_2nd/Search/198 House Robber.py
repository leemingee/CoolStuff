'''
Created by Ming Li at 2019-02-20

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        pre_max = cur_max = 0
        for i in range(len(nums)):
            cur_max, pre_max =  max(nums[i] + pre_max, cur_max), cur_max
        return cur_max
    
if __name__ == '__main__':
    res = Solution().rob([2,1,1,2])
    print(res)