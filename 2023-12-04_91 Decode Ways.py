# https://leetcode.com/problems/decode-ways/

class Solution: # T: 18.36% M: 69.43%
    #@ https://www.youtube.com/watch?v=6aEyTjOwlJU
    def numDecodings(self, s: str) -> int:
        # *** Dynamic Programming ***
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]

class Solution: # T: 43.50% M: 28.05%
    #@ https://www.youtube.com/watch?v=6aEyTjOwlJU
    def numDecodings(self, s: str) -> int:
        # *** Memoization ***
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)