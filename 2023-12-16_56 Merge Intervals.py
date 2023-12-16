# https://leetcode.com/problems/merge-intervals/

class Solution:  # T: 52.95% M: 30.54%
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                if interval[1] > result[-1][1]:
                    result[-1][1] = interval[1]
            else:
                result.append(interval)
        return result
