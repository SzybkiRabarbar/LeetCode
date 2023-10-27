#https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    # T: 9.73% M: 35.45%

    def isValid(self, s):
        stack = []
        data={"(":")","[":"]","{":"}"}
        for letter in s:
            if letter in data.keys():
                stack.append(data.get(letter))
            else:
                if not stack or not stack.pop()==letter: return False
        if stack: return False
        return True

if __name__=="__main__":
    s = "()[(])"
    print(Solution().isValid(s))