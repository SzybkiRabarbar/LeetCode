# https://leetcode.com/problems/permutation-in-string/

from string import ascii_lowercase

class Solution: # T: 33.32% M: 74.33%
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        length = len(s2)
        while r <= length:
            if self.isAnagram(s1, s2[l:r]):
                return True
            l += 1
            r += 1
        return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        for i in ascii_lowercase:
            if s.count(i)!=t.count(i):
                return False
        return True

class NotMySolution: # T: 63.93% M: 44.12%
    #@ https://youtu.be/UbyhOgBN834?si=1umIkikjrBie-ed2
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
