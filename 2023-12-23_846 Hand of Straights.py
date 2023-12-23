# https://leetcode.com/problems/hand-of-straights/
from collections import heapq


class Solution:  # T: 99.81% M: 5.16%
    # @ https://www.youtube.com/watch?v=amnrMCVd2YI
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        pass
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
