# https://leetcode.com/problems/jump-game-ii/

class Solution1:  # T: 27.17% M: 33.05% O(N^2)
    def jump(self, nums: list[int]) -> int:
        ln = len(nums) - 1
        if not ln:
            return 0
        buffor = [0] + [ln] * ln
        for i, n in enumerate(nums):
            curr = buffor[i] + 1
            if i + n >= ln:
                return curr
            for j in range(1, n + 1):
                c = i + j
                if buffor[c] > curr:
                    buffor[c] = curr


class Solution:  # T: 37.53% M: 88.01% O(N)
    def jump(self, nums: list[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res
