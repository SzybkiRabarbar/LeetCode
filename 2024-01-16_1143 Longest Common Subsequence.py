# https://leetcode.com/problems/longest-common-subsequence/

class Solution:  # T: 95.66% M: 44.82%
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        grid = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = 1 + grid[i + 1][j + 1]
                else:
                    grid[i][j] = max(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]
