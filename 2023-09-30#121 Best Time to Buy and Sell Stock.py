# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution: # T: 86.81% M: 48.36%
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        length = len(prices)
        
        if length == 1:
            return max_profit
        
        l, r = 0, 1
        
        while r < length:
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r = l + 1
            elif profit > max_profit:
                max_profit = profit
                r += 1
            else:
                r += 1
        
        return max_profit