# https://leetcode.com/problems/minimum-interval-to-include-each-query/

from collections import heapq


class BadSolution:  # DNF
    # BRUTEFORCE
    def minInterval(
            self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        result = []
        for q in queries:
            result.append(float('inf'))
            for left, right in intervals:
                if q >= left and q <= right:
                    curr = right - left + 1
                    if result[-1] > curr:
                        result[-1] = curr
            if result[-1] == float('inf'):
                result[-1] = -1
        return result


class Solution:  # T: 40.78% M: 68.24%
    # @ https://www.youtube.com/watch?v=5hQ5WWW5awQ
    def minInterval(
            self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
