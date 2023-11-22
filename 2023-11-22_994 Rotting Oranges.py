# https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution: # T: 54.68% M: 31.92$
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ln_row = len(grid)
        ln_col = len(grid[0])
        q = deque()
        for x in range(ln_row):
            for y in range(ln_col):
                if grid[x][y] == 2:
                    q.append((x, y))
        result = -1
        while q:
            result += 1
            for _  in range(len(q)):
                x, y = q.popleft()
                for ax, ay in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + ax, y + ay
                    if (
                        nx >= 0 and ny >= 0 and
                        nx < ln_row and ny < ln_col and
                        grid[nx][ny] == 1
                    ):
                        grid[nx][ny] = 2
                        q.append((nx, ny))
        
        for x in range(ln_row):
            for y in range(ln_col):
                if grid[x][y] == 1:
                    return -1
        return result if result >= 0 else 0
                    