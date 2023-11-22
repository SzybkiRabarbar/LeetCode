# https://leetcode.com/problems/surrounded-regions/

class Solution: # T: 43.37% M: 37.00%
    def solve(self, board: list[list[str]]) -> None:
        ln_row = len(board)
        ln_col = len(board[0])
        seen = set()
        def func(x, y):
            if (
                x >= 0 and y >= 0 and
                x < ln_row and y < ln_col and
                board[x][y] == 'O' and
                not (x, y) in seen
            ):
                seen.add((x, y))
                for ax, ay in [(-1,0), (1,0), (0,-1), (0,1)]:
                    func(x + ax, y + ay)
                
                
        for y in [0, ln_col - 1]:
            for x in range(ln_row):
                if board[x][y] == 'O' and not (x, y) in seen:
                    func(x, y)
        
        for x in [0, ln_row - 1]:
            for y in range(ln_col):
                if board[x][y] == 'O' and not (x, y) in seen:
                    func(x, y)
                    
        for x in range(1, ln_row - 1):
            for y in range(1, ln_col - 1):
                if board[x][y] == 'O' and not (x, y) in seen:
                    board[x][y] = 'X'