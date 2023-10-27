# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution: # T: 10.06% M: 64.15%
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        length = len(s)
        l, r = 0, 0
        counts = {s[r]: 1}
        while 1:
            letter = max(counts, key=counts.get)
            c = counts[letter]
            ln = len(s[l:r + 1])
            if ln - k <= c:
                r += 1
                if res < ln:
                    res = ln
                if r == length:
                    break
                
                if s[r] in counts:
                    counts[s[r]] += 1
                else:
                    counts[s[r]] = 1
            else:
                counts[s[l]] -= 1
                l += 1
        return res