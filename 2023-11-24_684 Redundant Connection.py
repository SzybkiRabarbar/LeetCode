# https://leetcode.com/problems/redundant-connection/

from collections import defaultdict, deque

class Solution: # T: 19.02% M: 21.82%
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        res_id = -1
        edges_map = defaultdict(list)
        for i, (x, y) in enumerate(edges):
            if edges_map[x] and edges_map[y]:
                seen = set()
                que = deque([x])
                while que:
                    for _ in range(len(que)):
                        next_ = que.popleft()
                        if next_ in seen:
                            continue
                        elif next_ == y:
                            res_id = i
                        seen.add(next_)
                        que.extend(edges_map[next_])
                
            edges_map[x].append(y)
            edges_map[y].append(x)
        return edges[res_id]

class Solution: # T: 71.75% M: 90.94%
    #@ https://www.youtube.com/watch?v=FXWRE67PLL0
    # * UnionFind
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
