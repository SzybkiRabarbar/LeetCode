# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zeros = [i for i, n in enumerate(nums) if not n]
        mult = 1
        if len(zeros) >= 2:
            return [0] * len(nums)
        elif len(zeros):
            for i, n in enumerate(nums):
                if i == zeros[0]:
                    continue
                mult *= n
            r = [0] * len(nums)
            r[zeros[0]] = mult
            return r

        for n in nums:
            mult *= n

        res = []
        for n in nums:
            res.append(int(mult / n))

        return res
