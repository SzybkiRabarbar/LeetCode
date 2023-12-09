# https://leetcode.com/problems/reducing-dishes/

import heapq

class Solution: # T: 99.54% M: 33.38%
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        heap = [-1*x for x in satisfaction]
        heapq.heapify(heap)
        is_worth = 0
        best_satisfaction = []
        while heap:
            head = heapq.heappop(heap)
            is_worth += head
            if is_worth > 0: break
            best_satisfaction.append(head)
        return sum((-i*x for i, x in enumerate(best_satisfaction[::-1], 1)))