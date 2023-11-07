# https://leetcode.com/problems/palindrome-partitioning/

from collections import deque

class Solution: # T: 5.06% M: 9.36%
    def partition(self, s: str) -> list[list[str]]:
        q = deque([[]])
        for i in range(len(s)):
            r = set()
            for _ in range(len(q)):
                subset = q.popleft()
                subset.append(s[i])
                q.append(subset.copy())
                r.add(tuple(subset))
                for _ in range(len(subset) - 1):
                    last = subset.pop(-1)
                    subset[-1] += last
                    if (
                        not tuple(subset) in r and
                        self.isPalindrome(subset[-1], 0, len(subset[-1]) - 1)
                    ):
                        q.append(subset.copy())
                        r.add(tuple(subset))
        return q
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True