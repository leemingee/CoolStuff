'''
Created by Ming Li at 2019-02-23

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def generatePalindromes(self, s):
        from collections import Counter
        valid = sum(v % 2 for k, v in Counter(s).items()) < 2
        if not valid:
            return []
        permute_ans = self.permuteUnique(s)
        return permute_ans
        # res = []
        # for each_ans in permute_ans:
        #     if self.judge_palindrome(each_ans):
        #         res.append(each_ans)
        # return res
    
    def permuteUnique(self, s):
        visited = len(s) * [False]
        permutes = []
        s = sorted(s)  # transfer from string to sorted list
        
        def backtracking(s, n, temp):
            if len(temp) == n:
                permutes.append(temp[:])
            for i in range(len(s)):
                if visited[i] == True:
                    continue
                if i > 0 and visited[i - 1] == True and s[i] == s[i - 1]:
                    continue
                visited[i] = True
                temp.append(s[i])
                backtracking(s, n, temp)
                temp.pop()
                visited[i] = False
        
        backtracking(s, len(s), [])
        permutes = [''.join(each) for each in permutes]
        return permutes
    
    def judge_palindrome(self, each_str):
        if not each_str:
            return False
        left = 0
        right = len(each_str) - 1
        while left <= right:
            if each_str[left] == each_str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

import itertools
import collections
class Solution2(object):
    def generatePalindromes(self, s):
        d = collections.Counter(s)
        m = tuple(k for k, v in d.iteritems() if v % 2)
        p = ''.join(k*(v/2) for k, v in d.iteritems())
        return [''.join(i + m + i[::-1]) for i in set(itertools.permutations(p))] if len(m) < 2 else []

class Solution3:
    def generatePalindromes(self, s):
        self.m = {}
        for c in s:
            if c not in self.m:
                self.m[c] = 0
            self.m[c] += 1
        
        oddCount = 0
        middle = ''
        for k in self.m.keys():
            if self.m[k] % 2:
                middle = k
                self.m[k] -= 1
                oddCount += 1
        
        if oddCount > 1:
            return []
        
        self.ans = []
        self.createPalin(middle)
        return self.ans
    
    def createPalin(self, s):
        noMore = True
        for k in self.m.keys():
            if self.m[k] == 0:
                continue
            self.m[k] -= 2
            self.createPalin(k + s + k)
            self.m[k] += 2
            noMore = False
        
        if noMore:
            self.ans.append(s)

if __name__ == '__main__':
    res = Solution().generatePalindromes("aabbhijkkjih")
    print(res)