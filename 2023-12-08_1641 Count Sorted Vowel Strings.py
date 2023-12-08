# https://leetcode.com/problems/count-sorted-vowel-strings/

from collections import deque

class Solution: # T: 12.16% M: 8.01%
    def countVowelStrings(self, n: int) -> int:
        chars = ["a","e","i","o","u"]
        queue = deque(chars)
        for _ in range(n - 1):
            for _ in range(len(queue)):
                match queue.popleft():
                    case "a":
                        x = 0
                    case "e":
                        x = 1
                    case "i":
                        x = 2
                    case "o":
                        x = 3
                    case "u":
                        x = 4
                for char in chars[x:]:
                    queue.append(char)
        return len(queue)

class Solution: # T: 66.89% M: 53.19%
    def countVowelStrings(self, n: int) -> int:
        chars_count = [1] * 5
        for _ in range(n - 1):    
            chars_count = [sum(chars_count[:i+1]) for i in range(5)]
        return sum(chars_count)