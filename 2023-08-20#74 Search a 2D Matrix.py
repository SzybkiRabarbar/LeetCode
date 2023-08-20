# https://leetcode.com/problems/search-a-2d-matrix/

class Solution1: # T: 39.51% M: 21.32%
    """
    Binary search on m then binary search on n (matrix[m*n])
    """
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        right = len(matrix)
        while left <= right:
            mid_m = (left + right) // 2
            if mid_m > len(matrix) - 1:
                return False
            if matrix[mid_m][0] <= target and matrix[mid_m][-1] >= target: #| If good section
                
                left = 0
                right = len(matrix[mid_m])
                while left <= right:
                    mid_n = (left + right) // 2
                    if matrix[mid_m][mid_n] == target:
                        return True
                    elif matrix[mid_m][mid_n] > target:
                        right = mid_n - 1
                    else:
                        left = mid_n + 1
                
            elif matrix[mid_m][0] > target:
                right = mid_m - 1
            else:
                left = mid_m + 1
        return False

class Solution2: # T: 42.93% M: 86.83%
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
