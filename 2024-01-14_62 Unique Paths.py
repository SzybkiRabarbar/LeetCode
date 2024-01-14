# https://leetcode.com/problems/unique-paths/

class Solution:  # T: 83.67% M: 21.15%
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] for _ in range(m)]
        grid[0] = [1] * n

        for i in range(m - 1):
            for j in range(n - 1):
                grid[i + 1].append(grid[i + 1][j] + grid[i][j + 1])

        return grid[m - 1][n - 1]
