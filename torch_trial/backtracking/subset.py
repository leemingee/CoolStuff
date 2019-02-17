'''
Created by Ming Li at 2019-02-17

Feature: 

Description:
https://www.jianshu.com/p/3ef0e4e1114d
https://www.youtube.com/watch?v=CUzm-buvH_8

Contact: ming.li2@columbia.edu
'''
class DFS:  # 也可以把 backtracking 当成 DFS
    def subsets(self, S):
        self.result = []
        self.backtrack(0, sorted(S), [])
        return self.result

    # 这个是模板啊~
    def backtrack(self, start, S, temp):
        self.result.append(temp[:]) # also use the [:] to represent copy()
        for i in range(start , len(S)):
            temp.append(S[i])
            # print(temp)
            self.backtrack(i + 1, S, temp)
            temp.pop()
            
solu = DFS()
result = solu.subsets(S = [2,3,5,7])
# print(result)


class solu2:
    '''
    time complexity: O(n * 2^n)
    space complexity: O(n) the recursion depth
    '''
    
    def subsets(self, nums):
        ans = []
        
        
        def dfs(n, start, curr):
            # combinations of Cm, n) if we use dfs(n, 0, []),
            # where m = len(nums), n is the n input
            if len(curr) == n:
                ans.append(curr.copy()) # must use copy() here, otherwise, it will be empty list
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(n, i+1, curr)
                curr.pop()
        
        for i in range(len(nums)+1):
            dfs(i, 0, [])
        return ans
    
solu2 = solu2()
result = solu2.subsets(nums = [2,3,5,7])
print(result)

'''
this problem can be tricky, the key point is to use
the recursion tree to understand the DFS goes when
first encounter this kinds of problem
'''


# method 2
# can only be applied for the combination, where we have something like the O(2^n)
# for the O(2^n), we get the bit operations into system

def subsets(nums):
    n = len(nums)
    ans = []
    # areturn [[nums[i] for i in range(n) if s & 1 << i > 0] for s in range(1 << n)]
    for s in range(1 << n):
        ans.append([nums[i] for i in range(n) if s & 1 << i > 0])
    return ans
# print(subsets([1,2,3]))


# last one - submission version
class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        '''
        # method 1: the bit operation
        ans = []
        n = len(nums)
        for s in range(1 << n):
            ans.append([nums[i] for i in range(n) if s & 1 << i > 0])
        return ans
        '''
        
        # method 2: the dfs and backtracking
        self.ans = []
        for i in range(len(nums)+1):
            self.backtracking(nums, i, 0, [])
        return self.ans
    
    def backtracking(self, nums, length, start, cur):
        if len(cur) == length:
            self.ans.append(cur[:])
            return
        for i in range(start, len(nums)):
            cur.append(nums[i])
            self.backtracking(nums, length, i + 1, cur)
            cur.pop()


print(Solution().subsets([1,2,3]))