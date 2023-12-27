# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution:  # T: 99.79% M: 5.68%
    def mergeTriplets(
            self, triplets: list[list[int]], target: list[int]) -> bool:
        curr = None
        for triplet in triplets:
            if all((tr <= ta for tr, ta in zip(triplet, target))):
                if curr:
                    curr = [max(c, tr) for c, tr in zip(curr, triplet)]
                else:
                    curr = triplet
                if curr == target:
                    return True
        return False
