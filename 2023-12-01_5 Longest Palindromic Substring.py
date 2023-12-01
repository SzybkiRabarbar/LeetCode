# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ln = len(s)
        result = (0, 1)
        for i in range(ln - 1):
            for left, right in [(i - 1, i + 1), (i, i + 1)]:
                while left >= 0 and right < ln:
                    if s[left] == s[right]:
                        if right + 1 - left > result[1] - result[0]: result = (left, right + 1)
                        left -= 1
                        right += 1
                    else:
                        break
        return s[result[0]:result[1]]