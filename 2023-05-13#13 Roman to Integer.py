# https://leetcode.com/problems/roman-to-integer/description/

class Solution(object):
    let = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
    def romanToInt(self, s):
        result = 0
        for i, x in enumerate(s):
            temp = self.let.get(x)
            if i==len(s)-1: return result+temp
            if temp<self.let.get(s[i+1]):
                result-=temp
                continue
            result+=temp