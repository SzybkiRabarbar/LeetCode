# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:  # T: 51.20% M: 9.09%
    def checkValidString(self, s: str) -> bool:
        curr, ast = 0, 0
        # Left to Right
        for char in s:
            match char:
                case '*':
                    ast += 1
                case '(':
                    curr += 1
                case ')':
                    curr -= 1
            if curr < 0:
                ast -= 1
                curr += 1
                if ast < 0:
                    return False
        curr, ast = 0, 0
        # Right to Left
        for char in reversed(s):
            match char:
                case '*':
                    ast += 1
                case '(':
                    curr -= 1
                case ')':
                    curr += 1
            if curr < 0:
                ast -= 1
                curr += 1
                if ast < 0:
                    return False
        return True
