'''
Created by Ming Li at 2019-02-17

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        '''
        # using the basic itertools in python3
        import itertools
        return list(itertools.permutations(nums))
        '''
        # using the dfs and backtracking
        self.nums = sorted(nums)
        self.ans = []
        self.used = [False] * len(nums)
        self.dfs(len(nums), [])
        return self.ans
    
    def dfs(self, n, cur):
        # print(cur)
        if len(cur) == n:
            self.ans.append(cur[:])
            return
        for i in range(len(self.nums)):
            if self.used[i]:
                continue
            if i > 0 and self.used[i - 1] and self.nums[i] == self.nums[i - 1]:
                # [NOTE] the key point is here, how to jump the next if the before has been visited and
                # the same with current elem
                continue
            else:
                self.used[i] = True
                cur.append(self.nums[i])
                self.dfs(n, cur)
                cur.pop()
                self.used[i] = False


Solution().permuteUnique([3,3,0,3])