# https://leetcode.com/problems/partition-labels/
from collections import defaultdict


class Solution:  # T: 90.57% M: 5.19%
    def partitionLabels(self, s: str) -> list[int]:
        h = defaultdict(list)
        order = []
        for i, char in enumerate(s):
            if not h[char]:
                order.append(char)
                h[char] = [i, i]
            else:
                h[char][1] = i

        results = [[-1, -1]]
        for char in order:
            lf, rg = h[char]
            if results[-1][1] > lf:
                results[-1][1] = max(rg, results[-1][1])
            else:
                results.append([lf, rg])

        return [rg - lf + 1 for lf, rg in results[1:]]
