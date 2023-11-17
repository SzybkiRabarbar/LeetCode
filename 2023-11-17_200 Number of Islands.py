# https://leetcode.com/problems/number-of-islands/

from collections import deque

class Solution: # T: 5.11% M: 18.99%
    def numIslands(self, grid: list[list[str]]) -> int:
        ln_row = len(grid)
        ln_col = len(grid[0])
        islands = []
        for row in range(ln_row):
            for col in range(ln_col):
                if grid[row][col] != '1':
                    continue
                not_discovered = True
                for island in islands:
                    if (row, col) in island:
                        not_discovered = False
                        break
                if not_discovered:
                    land = set((row, col))
                    que = deque([(row, col)])
                    while que:
                        res = que.pop()
                        r, c = res
                        if r > 0 and not (r - 1, c) in land and grid[r - 1][c] == '1':
                            land.add((r-1, c))
                            que.append((r-1, c))

                        if r < ln_row - 1 and not (r + 1, c) in land and grid[r + 1][c] == '1':
                            land.add((r+1, c))
                            que.append((r+1, c))
                            
                        if c > 0 and not (r, c - 1) in land and grid[r][c - 1] == '1':
                            land.add((r, c-1))
                            que.append((r, c-1))
                            
                        if c < ln_col - 1 and not (r, c + 1) in land and grid[r][c + 1] == '1':
                            land.add((r, c+1))
                            que.append((r, c+1))
                    islands.append(land)
        return len(islands)