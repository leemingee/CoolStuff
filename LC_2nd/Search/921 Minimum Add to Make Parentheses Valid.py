'''
Created by Ming Li at 2019-02-22

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal


class Solution2:
    def minAddToMakeValid(self, S: str) -> int:
        res = 0
        r_more = l_more = 0
        r_count = l_count = 0
        for i in range(len(S)):
            if S[i] == "(":
                l_count += 1
                # for the case of '))(', we need to clean the r_more
                if r_more != 0:
                    res += r_more
                    r_more = r_count = 0
                l_more = l_count - r_count
            elif S[i] == ")":
                r_count += 1
                # for the case of '()'
                if l_more != 0:
                    l_more -= 1
                    l_count -= 1
                    r_count -= 1
                r_more = r_count - l_count if r_count > l_count else 0
        return res + l_more + r_more


if __name__ == '__main__':
    res = Solution()
    print(res)