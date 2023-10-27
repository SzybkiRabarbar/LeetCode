#https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    # T: 22.15% M: 55.61%
    def isPalindrome(self, inp: str) -> bool:
        palindrome = str()
        for letter in inp.lower():
            if letter.isalnum():
                palindrome += letter
        return palindrome == palindrome[::-1]
    
    # T: 75.49% M: 79.78%
    def isPalindromeTwoPoiners(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            a = s[i].lower()
            b = s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i = i + 1
                    j = j - 1
                    continue
            i = i + (not a.isalnum())
            j = j - (not b.isalnum())
        return True