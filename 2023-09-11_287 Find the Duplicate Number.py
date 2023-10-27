# https://leetcode.com/problems/find-the-duplicate-number/

class Solution: # T: 90.15% M: 21.90%
    def findDuplicate(self, nums: list[int]) -> int:
        hash_t = set()
        for num in nums:
            if num in hash_t:
                return num
            hash_t.add(num)