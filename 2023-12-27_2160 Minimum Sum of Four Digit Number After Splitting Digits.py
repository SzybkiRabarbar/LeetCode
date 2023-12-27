# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:  # T: 61.28% M: 6.83%
    def minimumSum(self, num: int) -> int:
        nums = sorted(str(num))
        return int(nums[0] + nums[2]) + int(nums[1] + nums[3])
