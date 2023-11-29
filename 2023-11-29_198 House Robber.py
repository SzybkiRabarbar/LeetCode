# https://leetcode.com/problems/house-robber/

class Solution: # T: 96.63% M: 18.18%
    #@ https://www.youtube.com/watch?v=73r3KWiEvyk
    def rob(self, nums: list[int]) -> int:
        left, right = 0, 0

        for n in nums:
            temp = max(n + left, right)
            left = right
            right = temp
        return right
