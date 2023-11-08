# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from collections import deque

class Solution: # T: 67.68% M: 87.83%
    
    KEYBORD = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return None
        q = deque([''])
        for d in digits:
            for _ in range(len(q)):
                comb = q.popleft()
                for char in Solution.KEYBORD[d]:
                    q.append(comb + char)
        return q
    
class Solution: # T: 39.38% M: 87.83%
    
    KEYBORD = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return None
        
        LN = len(digits)
        result = []
        def backtrack(i, comb):
            if i == LN:
                result.append(comb)
            else:
                for char in Solution.KEYBORD[digits[i]]:
                    backtrack(i + 1, comb + char)
    
        backtrack(0, '')
        return result