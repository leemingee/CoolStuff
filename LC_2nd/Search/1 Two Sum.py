'''
Created by Ming Li at 2019-02-19

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        reverse_dict = {
            target-elem : idx for idx, elem in enumerate(nums)
        }
        for j in range(len(nums)):
            i = reverse_dict.get(nums[j], None)
            if i is not None and i != j:
                return [i, j]

if __name__ == '__main__':
    res = Solution().twoSum([2,7,11,15], 9)
    print(res)