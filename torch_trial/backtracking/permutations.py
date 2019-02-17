'''
Created by Ming Li at 2019-02-17

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        '''
        # using the basic itertools in python3
        import itertools
        return list(itertools.permutations(nums))
        '''
        # using the dfs and backtracking
        self.nums = nums
        self.ans = []
        self.used = [False] * len(nums)
        self.dfs(len(nums), [])
        return self.ans
    
    def dfs(self, n, cur):
        if len(cur) == n:
            self.ans.append(cur[:])
            return
        for i in range(len(self.nums)):
            if self.used[i]:
                continue
            else:
                self.used[i] = True
                cur.append(self.nums[i])
                self.dfs(n, cur)
                cur.pop()
                self.used[i] = False


class Solution2:
    
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        ans = []
        
        def dfs(nums, temp):
            if len(temp) == len(nums):
                ans.append(temp[:])
            
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                dfs(nums, temp)
                temp.pop()
                
        dfs(nums, [])
        return ans
    
print(Solution2().permute(nums = [1,2,3]))