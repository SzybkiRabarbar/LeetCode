# https://leetcode.com/problems/counting-bits/

class Solution:  # T: 91.92% M: 15.29%
    def countBits(self, n: int) -> list[int]:
        res = [0, 1]
        if not n:
            return [0]
        elif n == 1:
            return res
        c = 1
        while True:
            for x in res.copy():
                c += 1
                res.append(x + 1)
                if c == n:
                    return res
