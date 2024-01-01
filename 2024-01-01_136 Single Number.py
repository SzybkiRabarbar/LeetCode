# https://leetcode.com/problems/single-number/

class SolutionHashMap:  # T: 98.26% M: 7.25%
    # non constant space
    def singleNumber(self, nums: list[int]) -> int:
        hash_map = dict()
        for n in nums:
            if n not in hash_map:
                hash_map[n] = True
            else:
                hash_map[n] = False

        for key, val in hash_map.items():
            if val:
                return key


class Solution:  # T: 94.83% M: 7.25%
    def singleNumber(self, nums: list[int]) -> int:
        r = 0
        for n in nums:
            r ^= n
        return r
