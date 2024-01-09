# https://leetcode.com/problems/network-delay-time/
from collections import heapq


class Solution:  # T: 96.95% M: 14.82%
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges = [[] for _ in range(n)]
        for u, v, w in times:
            edges[u - 1].append((v - 1, w))
        seen = [False] * (n + 1)
        seen_counter = 0
        queue = [(0, k - 1)]
        while queue:
            time, node = heapq.heappop(queue)
            if seen[node]:
                continue
            seen[node] = True
            seen_counter += 1
            if seen_counter == n:
                return time
            for next_node, travel_time in edges[node]:
                if seen[next_node]:
                    continue
                heapq.heappush(queue, (time + travel_time, next_node))
        return -1
