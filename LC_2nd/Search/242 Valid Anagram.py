'''
Created by Ming Li at 2019-02-23

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)

if __name__ == '__main__':
    res = Solution()
    print(res)