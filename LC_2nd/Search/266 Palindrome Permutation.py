'''
Created by Ming Li at 2019-02-23

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''

from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_dict = {}
        for elem in s:
            if elem not in char_dict:
                char_dict[elem] = 1
            else:
                char_dict[elem] = char_dict[elem] + 1
        ans = False
        odd_counts = 0
        for key, value in char_dict.items():
            if value % 2 == 0:
                pass
            else:
                odd_counts += 1
        
        return odd_counts <= 1

    def canPermutePalindrome2(self, s:str) -> bool:
        return sum(v % 2 for k, v in Counter(s).iteritems()) < 2
    
if __name__ == '__main__':
    res = Solution()
    print(res)