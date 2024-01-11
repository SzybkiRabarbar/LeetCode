# https://leetcode.com/problems/swim-in-rising-water/description/

class Solution:  # T: 98.17% M: 9.20%
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        fin = (n - 1, n - 1)
        flooded = set()
        edges = {grid[0][0]: (0, 0)}
        t = grid[0][0] - 1

        def func(cords: tuple[int]) -> bool:
            if cords == fin:
                return True
            x, y = cords
            if (cords in flooded
                    or x < 0 or x >= n
                    or y < 0 or y >= n):
                return False

            if grid[x][y] > t:
                edges[grid[x][y]] = cords
            else:
                flooded.add(cords)
                for sx, sy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if func((x + sx, y + sy)):
                        return True
            return False

        while True:
            t += 1
            if t in edges:
                if func(edges[t]):
                    return max(t, grid[n - 1][n - 1])
