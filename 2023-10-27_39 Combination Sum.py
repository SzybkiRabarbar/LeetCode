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
        