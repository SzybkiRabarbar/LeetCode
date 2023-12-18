# https://leetcode.com/problems/maximum-subarray/

class Solution:  # T: 32.14% M: 31.73%
    def maxSubArray(self, nums: list[int]) -> int:
        result = nums[-1]
        temp = nums[-1]
        for n in reversed(nums[:-1]):
            temp = max(temp + n, n)
            result = max(result, temp)
        return result
