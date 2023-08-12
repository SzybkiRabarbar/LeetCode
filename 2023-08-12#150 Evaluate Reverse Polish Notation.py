#https://leetcode.com/problems/evaluate-reverse-polish-notation/
from collections import deque

class Solution: # T: 98.13% M: 85.4%
    def evalRPN(self, tokens: list[str]) -> int:
        stack = deque()
        for token in tokens:
            if token.isnumeric():
                stack.append(int(token))
            elif token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                temp = stack.pop()
                stack.append(stack.pop() - temp)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                temp = stack.pop()
                res = stack.pop() / temp
                if res.is_integer():
                    stack.append(int(res))
                else:
                    stack.append(int(res // 1) if res >= 0 else int(res // 1) + 1)
            else:
                stack.append(int(token))
        return stack.pop()

if __name__=='__main__':
    print()
    s = Solution()
    print(s.evalRPN(["4","-2","/","2","-3","-","-"]))
