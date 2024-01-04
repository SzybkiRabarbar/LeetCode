# https://leetcode.com/problems/reverse-bits/

class Solution:  # T: 94.77% M: 12.90%
    def reverseBits(self, n: int) -> int:
        bin = format(n, 'b').zfill(32)
        return int(bin[::-1], 2)
