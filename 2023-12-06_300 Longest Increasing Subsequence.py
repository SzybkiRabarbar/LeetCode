# https://leetcode.com/problems/longest-increasing-subsequence/

from collections import defaultdict

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        hashM = defaultdict(int)
        for n in nums[::-1]:
            b = 0
            for key, val in hashM.items():
                if n < key and b < val:
                    b = val
            b += 1
            if b > hashM[n]:
                hashM[n] = b
        return max(hashM.values())