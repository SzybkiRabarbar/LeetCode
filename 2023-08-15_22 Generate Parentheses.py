# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]: #T: 68.15% M: 26.73%
        content = ['(']
        for _ in range(n + (n - 1)):
            temp = []
            for c in content:
                open = c.count('(')
                close = c.count(')')
                if open < n:
                    temp.append(c + '(')
                if close < n and close < open:
                    temp.append(c + ')')
            content = temp.copy()
        return content
    
if __name__=='__main__':
    s = Solution()
    print(s.generateParenthesis(4))