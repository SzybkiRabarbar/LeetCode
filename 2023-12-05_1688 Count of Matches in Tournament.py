# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution: # T: 32.17% M: 71.13%
    def numberOfMatches(self, n: int) -> int:
        r = 0
        while n != 1:
            if n % 2:
                n = ((n - 1) // 2)
                r += n
                n += 1
            else:
                n = n // 2
                r += n
        return r
    
class Solution: # T: 83.83% M: 5.91%
    def numberOfMatches(self, n: int) -> int:
        return n - 1