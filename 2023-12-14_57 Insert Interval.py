# https://leetcode.com/problems/insert-interval/

class Solution:  # T: 68.32% M: 30.06%
    def insert(self, intervals: list[list[int]], n_in: list[int]) -> list[list[int]]:
        if not intervals:
            return [n_in]
        elif intervals[0][0] > n_in[1]:
            return [n_in] + intervals
        lp, rp = None, len(intervals)
        curr = None
        for i, inter in enumerate(intervals):
            if not curr:
                lp = i
                if inter[0] >= n_in[0]:
                    if inter[0] > n_in[1]:
                        return intervals[:lp] + [n_in] + intervals[lp:]
                    curr = [n_in[0], max(inter[1], n_in[1])]
                elif inter[1] >= n_in[0]:
                    curr = [inter[0], max(inter[1], n_in[1])]
            else:
                if inter[0] > curr[1]:
                    rp = i
                    break
                elif inter[1] >= curr[1]:
                    rp = i + 1
                    curr[1] = inter[1]
                    break
        if not curr:
            return intervals + [n_in]
        return intervals[:lp] + [curr] + intervals[rp:]
