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