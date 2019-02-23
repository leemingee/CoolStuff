'''
Created by Ming Li at 2019-02-23

Feature: 

Description:

https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.

Contact: ming.li2@columbia.edu
'''
from collections import Counter
class Solution:
    # naive way, time too much
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        m = len(p)
        for start in range(len(s)-m+1):
            temp = s[start: start+m]
            if Counter(temp) == Counter(p):
                ans.append(start)
        return ans
    
    
class Solution2:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            sCounter[s[i]] += 1  # include a new char in the window
            if sCounter == pCounter:  # This step is O(1), since there are at most 26 English letters
                res.append(i - len(p) + 1)  # append the starting index
            sCounter[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]  # remove the count if it is 0
        return res


class Solution3(object):
    def findAnagrams(self, s, p):
        if len(s) < len(p) or not s or not p:
            return []
        
        need = Counter(p)
        res = []
        l, r, missing = 0, 0, len(p)
        
        while r < len(s):
            if need[s[r]] > 0:
                missing -= 1
            need[s[r]] -= 1
            
            if missing == 0:
                res.append(l)
            
            if r - l == len(p) - 1:
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1
            
            r += 1
        
        return res
if __name__ == '__main__':
    res = Solution()
    print(res)