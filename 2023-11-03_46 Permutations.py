# https://leetcode.com/problems/permutations/

from itertools import permutations

class Solution: # T: 43.91% M: 75.44%
    def permute(self, nums: list[int]) -> list[list[int]]:
        return [x for x in permutations(nums, len(nums))]

class Solution: # T: 80.32% M: 75.44%
    #@ https://www.youtube.com/watch?v=s7AvT7cGdSo
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]  

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res

class Solution: # T: 55.24% M:92.51%
    def permute(self, nums: list[int], r = None) -> list[list[int]]:
        if r is None:
            r = []
        if not nums:
            return [r]
        res = []
        for i in range(len(nums)):
            res.extend(self.permute(nums[:i] + nums[i + 1:], r + [nums[i]]))
        return res