# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque

class Solution: #T: 64.49% M: 66.43%
    # @ https://www.youtube.com/watch?v=DfljaUwZsOk
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
