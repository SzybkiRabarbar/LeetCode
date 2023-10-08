# https://leetcode.com/problems/minimum-window-substring/

from string import ascii_lowercase, ascii_uppercase

class Solution: # T: 14.88% M: 99.78%
    def minWindow(self, s: str, t: str) -> str:
        result_len = 0
        len_t, len_s = len(t), len(s)
        if len_t > len_s:
            return ''
        hash_t = {x: t.count(x) for x in t}
        hash_s = {x: 0 for x in ascii_uppercase + ascii_lowercase}
        l, r = 0, len_t - 1
        
        for i in range(len_t):
            hash_s[s[i]] += 1
        
        while r < len_s:
            missing = False
            
            for t_key, t_val in hash_t.items():
                if hash_s[t_key] < t_val:
                    missing = True
                    break
            
            if missing:
                r += 1
                if r >= len_s:
                    break
                hash_s[s[r]] += 1
            else:
                lenght = r - l + 1
                if not result_len or result_len > lenght:
                    result_len = lenght
                    result_pos = (l, r)
            
                hash_s[s[l]] -= 1
                l += 1
        if result_len:
            return s[result_pos[0]:result_pos[1] + 1]
        else:
            return ''