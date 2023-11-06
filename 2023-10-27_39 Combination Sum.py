# https://leetcode.com/problems/combination-sum/

from collections import deque

class Solution: # T: 39.45% M: 12.19%
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = [x for x in candidates if x <= target]
        queue = deque([[x] for x in candidates])
        result = []
        while queue:
            for _ in range(len(queue)):
                q = queue.popleft()
                sum_ = sum(q)
                if sum_ == target:
                    result.append(q)
                elif sum_ < target:
                    for num in candidates:
                        if q[-1] <= num:
                            queue.append(q + [num])
        return result

class Solution: # T: 77.26% M: 30.37%
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        combs = [[]]
        res = []
        for c in candidates:
            if c > target:
                continue
            if c == target:
                res.append([c])
                continue
            for i in range(len(combs)):
                sum_ = sum(combs[i]) + c
                if sum_ == target:
                    res.append(combs[i] + [c])
                elif sum_ < target:
                    combs.append(combs[i] + [c])
                    while (sum_ + c) < target:
                        sum_ += c
                        combs.append(combs[-1] + [c])
                    if (sum_ + c) == target:
                        res.append(combs[-1] + [c])
        return res