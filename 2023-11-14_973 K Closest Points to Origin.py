# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq

class Solution: # T: 76.69% M: 23.10%
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            dist = (((x * x) + (y * y)) * -1, [x, y])
            if len(heap) == k:
                max_ = heapq.heappop(heap)
                if max_ < dist:
                    heapq.heappush(heap, dist)    
                else:
                    heapq.heappush(heap, max_)
            else:
                heapq.heappush(heap, dist)
        return [cords for _, cords in heap]