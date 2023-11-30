# https://leetcode.com/problems/house-robber-ii/

class Solution: # T: 47.37% M: 20.19%
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        def dp(arr: list[int]) -> int:
            left, right = 0, 0
            for n in arr:
                temp = max(left + n, right)
                left = right
                right = temp
            return right
        return max(dp(nums[:-1]), dp(nums[1:]))