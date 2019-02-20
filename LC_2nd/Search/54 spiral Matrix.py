'''
Created by Ming Li at 2019-02-19

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        # using recursion
        m, n = len(matrix), len(matrix[0])
        if not matrix:
            return []
        self.ans = []
        r1, r2 = 0, m - 1
        c1, c2 = 0, n - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in self.spiral_coords(r1, c1, r2, c2):
                self.ans.append(matrix[r][c])
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return self.ans
    
    def spiral_coords(self, r1, c1, r2, c2):
        for c in range(c1, c2 + 1):
            yield r1, c
        for r in range(r1 + 1, r2 + 1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1


if __name__ == '__main__':
    testcase = [[1,2,3],[4,5,6],[7,8,9]]
    res = Solution().spiralOrder(matrix=testcase)
    print(res)