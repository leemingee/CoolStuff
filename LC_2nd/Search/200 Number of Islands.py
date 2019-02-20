'''
Created by Ming Li at 2019-02-19

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''


class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        # using dfs to find the connected component
        
        # corner case
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, m, n)
                    count += 1
        return count
    
    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
            return
        grid[i][j] = -1
        self.dfs(grid, i + 1, j, m, n)
        self.dfs(grid, i, j + 1, m, n)
        self.dfs(grid, i - 1, j, m, n)
        self.dfs(grid, i, j - 1, m, n)


if __name__ == '__main__':
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    res = Solution().numIslands(grid)
    print(res)