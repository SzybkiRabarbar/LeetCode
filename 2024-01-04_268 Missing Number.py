# https://leetcode.com/problems/missing-number/

class Solution1:  # T: 97.86% M: 5.12%
    # O(n) memory !!
    def missingNumber(self, nums: list[int]) -> int:
        hash_table = set(nums)
        for i in range(len(nums) + 1):
            if i not in hash_table:
                return i


class Solution2:  # T: 96.1% M: 9.33%
    # O(1) memory
    def missingNumber(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        for i in range(len(nums) + 1):
            res ^= i
        return res
