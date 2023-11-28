# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution: # T: 37.02% M: 37.59%
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        left, right = cost[-2], cost[-1]
        for i in range(len(cost) - 2):
            curr = cost[-3 - i]
            if left < right:
                curr += left
            else:
                curr += right
            left, right = curr, left
        return left if left < right else right