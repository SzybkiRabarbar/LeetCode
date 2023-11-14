# https://leetcode.com/problems/last-stone-weight/

import heapq

class Solution: # T: 53.07% M: 7.23%
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [rock * -1 for rock in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            rock1 = heapq.heappop(stones)
            rock2 = heapq.heappop(stones)
            residues = rock1 - rock2
            if residues:
                heapq.heappush(stones, residues)
        
        if stones:
            return stones[0] * -1
        else:
            return 0