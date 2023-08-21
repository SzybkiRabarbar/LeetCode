# https://leetcode.com/problems/koko-eating-bananas/

from math import ceil

class Solution: # T: 98.86% M: 46.47%
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles) + 1
        result = right
        while left <= right:
            mid = (right + left) // 2
            time = sum([ceil(bananas / mid) for bananas in piles])
            if time <= h:
                if result > mid:
                    result = mid 
                right = mid - 1
            else:
                left = mid + 1
        return result
        
            
            
        
if __name__=="__main__":
    s = Solution()
    # print(s.minEatingSpeed(piles = [3,6,7,11], h = 8))
    # print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
    # print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 6))
    # print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 7))
    # print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 8))
    print(s.minEatingSpeed([2], 2))
    
    ## print(s.minEatingSpeed())