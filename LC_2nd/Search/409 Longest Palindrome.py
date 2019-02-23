'''
Created by Ming Li at 2019-02-23

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = {}
        for elem in s:
            if elem not in char_dict:
                char_dict[elem] = 1
            else:
                char_dict[elem] = char_dict[elem] + 1
        ans = 0
        exists_odd = 0
        for key, value in char_dict.items():
            if value % 2 == 0:
                ans += value
            else:
                exists_odd = 1
                ans += (value // 2) * 2
        
        return ans + exists_odd

if __name__ == '__main__':
    res = Solution()
    print(res)