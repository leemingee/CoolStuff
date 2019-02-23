'''
Created by Ming Li at 2019-02-22

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_len = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            
            usedChar[s[i]] = i
        
        return max_len


class Solution2:
    # not using sliding window, O(n^2) check for each start one by one
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start = end = 0
        ans = 0
        chars = set()
        while start < n and end <= n - 1:
            if s[end] not in chars:
                chars.add(s[end])
                ans = max(ans, end - start + 1)
                end += 1
            else:  # s[end] in chars
                chars = set()
                start += 1
                end = start
                ans = max(ans, end - start + 1)
        return ans


if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring("pewsdwds")
    print(res)