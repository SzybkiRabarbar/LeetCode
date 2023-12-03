# https://leetcode.com/problems/palindromic-substrings/

class Solution: # T: 83.41% M: 84.58%
    def countSubstrings(self, s: str) -> int:
        result = len(s)
        ln = len(s)
        
        for i in range(1, ln):
            for l, r in [(i - 1, i), (i - 1, i + 1)]:
                if r == ln: continue
                while (
                    l >= 0 and
                    r < ln and
                    s[l] == s[r]
                ):
                    result += 1
                    l -= 1
                    r += 1
        return result