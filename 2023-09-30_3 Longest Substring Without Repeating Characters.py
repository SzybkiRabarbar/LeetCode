# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution1: # T: 9.11% M: 93.33%
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_n = 0
        n = 0
        length = len(s)
        content = set()
        l, r = 0, 0
        
        while r < length:
            if s[r] in content:
                if n > longest_n:
                    longest_n = n
                content = set()
                n = 0
                l += 1
                r = l
            content.add(s[r])
            r += 1
            n += 1
        
        if n > longest_n:
            longest_n = n
        return longest_n

class Solution2: # T: 81.73% M: 93.33%
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_n = 0
        length = len(s)
        content = ""
        l, r = 0, 0
        
        while r < length:
            if s[r] in content:
                if len(content) > longest_n:
                    longest_n = len(content)
                id = content.index(s[r]) + 1
                l += id
                content = content[id::]
            content += s[r]
            r += 1
        
        if len(content) > longest_n:
            longest_n = len(content)
        return longest_n
