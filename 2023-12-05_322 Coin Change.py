# https://leetcode.com/problems/coin-change/

class Solution: # T: 93.25% M: 31.91%
    def coinChange(self, coins: list[int], amount: int) -> int:
        results = {0: 0}
        for i in range(1, amount + 1):
            for c in coins:
                s = i - c
                if s < 0 or not s in results: continue
                if not i in results or results[i] > results[s] + 1:
                    results[i] = results[s] + 1
        return results[amount] if amount in results else -1

class Solution: # T: 94.37% M: 44.78%
    def coinChange(self, coins: list[int], amount: int) -> int:
        results = [0]
        for i in range(1, amount + 1):
            results.append(-1)
            for c in coins:
                s = i - c
                if s < 0 or results[s] == -1: continue
                if results[i] == -1 or results[i] > results[s] + 1:
                    results[i] = results[s] + 1
        return results[amount]