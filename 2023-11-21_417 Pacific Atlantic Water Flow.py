# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution: # T: 5.01% M: 82.10%
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ln_row = len(heights)
        ln_col = len(heights[0])
        
        def func(x: int, y: int, prev: int, seen: set):
            if x < 0 or y < 0:
                self.pacific = True
            elif x >= ln_row or y >= ln_col:
                self.atlantic = True
            elif not (self.pacific and self.atlantic) and not (x, y) in seen and prev >= heights[x][y]:
                new_prev = heights[x][y]
                seen.add((x, y))
                func(x-1, y, new_prev, seen)
                func(x+1, y, new_prev, seen)
                func(x, y-1, new_prev, seen)
                func(x, y+1, new_prev, seen)
                seen.remove((x, y))
                
        result = []
        for x in range(ln_row):
            for y in range(ln_col):
                self.pacific = False
                self.atlantic = False
                prev = heights[x][y]
                func(x, y, prev, set())
                if self.pacific and self.atlantic:
                    result.append([x, y])
        return result