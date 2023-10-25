# https://leetcode.com/problems/subsets/

from collections import deque

class Solution: # T: 89.07% M: 55.43%
    def subsets(self, nums: list[int]) -> list[list[int]]:
        queue = deque([[]])
        for n in nums:
            for _ in range(len(queue)):
                subset = queue.popleft()
                queue.append(subset)
                queue.append(subset + [n])
        return list(queue)
    
s = Solution()
r = s.subsets([1,2,3])
print(r)
