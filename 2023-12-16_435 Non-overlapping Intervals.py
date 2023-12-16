# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:  # T: 66.21% M: 56.79%
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        non_overlapping = [intervals[0]]  # not accurate list
        for interval in intervals[1:]:
            if interval[0] < non_overlapping[-1][1]:
                non_overlapping[-1][1] = min(
                    non_overlapping[-1][1], interval[1])
            else:
                non_overlapping.append(interval)
        return len(intervals) - len(non_overlapping)
