'''
Created by Ming Li at 2019-02-23

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force, using O(n^3)
        if not s:
            return ""
        n = len(s)
        max_len = 0
        res = s[0]
        for i in range(n):
            for j in range(i, n, 1):
                temp = s[i:j + 1]
                # check if the temp is palindromic
                temp_reverse = temp[::-1]
                if temp_reverse == temp:
                    res = temp if len(temp) > max_len else res
                    max_len = max(max_len, len(temp))
        return res

class Solution2(object):
    def longestPalindrome(self, s):
        ans = ''
        max_len = 0
        n = len(s)
        DP = [[0] * n for _ in xrange(n)]
        for i in xrange(n):
            DP[i][i] = True
            max_len = 1
            ans = s[i]
        for i in xrange(n-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
                ans = s[i:i+2]
                max_len = 2
        for j in xrange(n):
            for i in xrange(0, j-1):
                if s[i] == s[j] and DP[i+1][j-1]:
                    DP[i][j] = True
                    if max_len < j - i + 1:
                        ans = s[i:j+1]
                        max_len = j - i + 1
        return ans


class Solution3:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]: return s
        
        start, max_length = 0, 1
        for i in range(1, len(s)):
            if i - max_length >= 1:
                temp = s[i - max_length - 1: i + 1]
                if temp == temp[::-1]:
                    start = i - max_length - 1
                    max_length += 2
                    continue
            
            temp = s[i - max_length: i + 1]
            if temp == temp[::-1]:
                start = i - max_length
                max_length += 1
        return s[start: start + max_length]

if __name__ == '__main__':
    res = Solution()
    print(res)