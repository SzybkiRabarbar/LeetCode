# https://leetcode.com/problems/number-of-1-bits/

class Solution1:  # T: 5.52% M: 6.84%
    def hammingWeight(self, n: int) -> int:
        res = 0
        pos = 32
        while n:
            num = 2**pos
            if num <= n:
                res += 1
                n -= num
            pos -= 1
        return res
