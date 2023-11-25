# https://www.lintcode.com/problem/663/
# https://leetcode.com/problems/walls-and-gates/

from collections import deque

class Solution:
    def walls_and_gates(self, rooms: list[list[int]]):
        ln_row = len(rooms)
        ln_col = len(rooms[0])
        for x in range(len(rooms)):
            for y in range(len(rooms[0])):
                que = deque([(x, y)])
                result = -1
                exit_ = False
                while que and not exit_:
                    result += 1
                    for _ in range(len(que)):
                        i, j = que.popleft()
                        if not (i >= 0 and j >= 0 and
                            i < ln_row and j < ln_col
                        ): continue
                        
                        val = rooms[i][j]
                        if not val:
                            exit_ = True
                            break
                        elif val > 0:
                            for ai, aj in [(-1,0), (1,0), (0,-1), (0,1)]:
                                que.append((i + ai, j + aj))
                
                if result: rooms[x][y] = result
        
if __name__=="__main__":
    s = Solution()
    inp = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    s.walls_and_gates(inp)
    print(inp)
             
"""
Input:
[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output:
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
"""