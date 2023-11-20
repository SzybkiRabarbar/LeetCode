# https://leetcode.com/problems/max-area-of-island/

class Solution: # T: 75.28% M: 22.59%
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        row_ln = len(grid)
        col_ln = len(grid[0])
        result = 0
        self.temp_res = 0
        def func(x, y):
            if (x >= 0 and
                x < row_ln and 
                y >= 0 and
                y < col_ln and
                grid[x][y]
            ):
                grid[x][y] = 0
                self.temp_res += 1
                func(x-1, y)
                func(x+1, y)
                func(x, y-1)
                func(x, y+1)
                
            
        for row_i in range(row_ln):
            for col_i in range(col_ln):
                if grid[row_i][col_i]:
                    func(row_i, col_i)
                if self.temp_res > result:
                    result = self.temp_res
                self.temp_res = 0
        return result