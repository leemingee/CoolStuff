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

if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring("pewsdwds")
    print(res)