'''
Created by Ming Li at 2019-02-19

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        reverse_dict = {
            -elem: i for i, elem in enumerate(nums)
        }
        self.ans = set()
        for idx in range(len(nums)):
            output = self.twoSum(nums[:idx] + nums[idx:], -nums[idx])
            if output != [-1, -1]:
                output.append(idx)
                temp = sorted([nums[i] for i in output])
                temp = tuple(temp)
                self.ans.add(temp[:])
        return self.ans
    
    def twoSum(self, nums, target):
        reverse_dict = {
            target - elem: i for i, elem in enumerate(nums)
        }
        
        for j in range(len(nums)):
            i = reverse_dict.get(nums[j], None)
            if i is not None and i != j:
                return [i, j]
            else:
                return [-1, -1]

class Solution2:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1;
                    r -= 1
        return res

if __name__ == '__main__':
    testcase = [-1, 0, 1, 2, -1, -4]
    res = Solution().threeSum(nums = testcase)
    print(res)