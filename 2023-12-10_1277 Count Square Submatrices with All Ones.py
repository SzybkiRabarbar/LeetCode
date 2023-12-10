# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution: # T: 51.80% M: 24.10%
    def countSquares(self, matrix: list[list[int]]) -> int:
        temp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        result = 0
        for i, m in enumerate(matrix):
            for j, n in enumerate(m):
                if not n: continue
                temp[i][j] = 1
                if i > 0 and j > 0:
                    temp[i][j] += min(temp[i - 1][j], temp[i][j - 1], temp[i - 1][j - 1])
                result += temp[i][j]
        return result