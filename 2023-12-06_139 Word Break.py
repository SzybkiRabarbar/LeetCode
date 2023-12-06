# https://leetcode.com/problems/word-break/

class Solution: # T: 46.62% M: 42.87%
    #@ https://www.youtube.com/watch?v=Sx9NNgInc3A
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]