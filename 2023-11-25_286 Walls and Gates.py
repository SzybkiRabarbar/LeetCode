# https://www.lintcode.com/problem/663/
# https://leetcode.com/problems/walls-and-gates/

from collections import deque

class Solution1:
    def walls_and_gates(self, rooms: list[list[int]]):
        ln_row = len(rooms)
        ln_col = len(rooms[0])
        for x in range(len(rooms)):
            for y in range(len(rooms[0])):
                que = deque([(x, y)])
                result = -1
                seen = set()
                exit_ = False
                while que and not exit_:
                    result += 1
                    for _ in range(len(que)):
                        i, j = que.popleft()
                        if not (i >= 0 and j >= 0 and i < ln_row and j < ln_col):
                            continue
                        elif (i, j) in seen:
                            continue
                        else:
                            seen.add((i, j))
                        
                        val = rooms[i][j]
                        if not val:
                            exit_ = True
                            break
                        elif val > 0:
                            for ai, aj in [(-1,0), (1,0), (0,-1), (0,1)]:
                                que.append((i + ai, j + aj))
                
                if result and exit_: rooms[x][y] = result
                
class Solution:
    #@ https://www.youtube.com/watch?v=e69C6xhiSQE
    def walls_and_gates(self, rooms: list[list[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRooms(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or rooms[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1

if __name__=="__main__":
    s = Solution()
    inp = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    s.walls_and_gates(inp)
    print(inp)