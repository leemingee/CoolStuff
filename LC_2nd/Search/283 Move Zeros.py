'''
Created by Ming Li at 2019-02-19

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        lastNonZeroIdx = 0
        while cur < len(nums):
            if nums[cur] != 0:
                self.swap(nums, cur, lastNonZeroIdx)
                lastNonZeroIdx += 1
            cur += 1
        return nums
    '''
    Therefore,
    - when we encounter a non-zero element,
    we need to swap elements pointed by current and slow pointer,
    then advance both pointers.
    
    - If it's zero element, we just advance current pointer.
    '''
    
    def swap(self, nums, left, right):
        temp = nums[right]
        nums[right] = nums[left]
        nums[left] = temp
    
    def moveZeroes2(self, nums):
        i = 0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                end -= 1
            else:
                i += 1


if __name__ == '__main__':
    res = Solution().moveZeroes([1,0,1,2,0,0,2])
    print(res)