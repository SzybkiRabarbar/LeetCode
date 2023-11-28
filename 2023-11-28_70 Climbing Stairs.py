# https://leetcode.com/problems/climbing-stairs/

class Solution: # T: 70.69% M: 9.18%
    def climbStairs(self, n: int) -> int:
        c1, c2 = 1, 1
        for _ in range(n - 1):
            c1, c2 = c1 + c2, c1
        return c1