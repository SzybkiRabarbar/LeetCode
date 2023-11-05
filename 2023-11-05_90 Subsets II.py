# https://leetcode.com/problems/subsets-ii/

from collections import deque

class Solution: # T: 27.41% M: 87.62%
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = {'': []}
        q = deque([[]])
        for n in nums:
            for _ in range(len(q)):
                subset = q.popleft()
                q.append(subset)
                q.append(subset + [n])
                name = ''.join(str(sorted(subset + [n])))
                res[name] = subset + [n]
        return res.values()
     
class Solution: # T: 92.28% M: 61.91%
    #@ https://www.youtube.com/watch?v=Vn2v6ajA7U0
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
