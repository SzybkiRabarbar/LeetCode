# https://leetcode.com/problems/n-queens/

class Solution: # T: 55.03% M: 52.29%
    def solveNQueens(self, n: int) -> list[list[str]]:
        if n == 1:
            return [['Q']]
        elif n < 4:
            return []
        
        result = []
        def backtrack(cords, board):
            row = len(cords)
            if row == n:
                result.append(board)
                return None
            
            is_valid = [True for _ in range(n)]
            for i, cord in enumerate(cords):
                is_valid[cord] = False
                diff = row - i
                if cord - diff >= 0:
                    is_valid[cord - diff] = False
                if cord + diff <= n - 1:
                    is_valid[cord + diff] = False

            for i, v in enumerate(is_valid):
                if v:
                    r = '.' * i
                    o = 'Q'
                    w = '.' * (n - i - 1)
                    backtrack(cords + [i], board + [r+o+w])
            
        backtrack([], [])
        return result
        
        
            