# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution: # T: 97.61% M: 63.40%
    
    def canPartition(self, nums: list[int]) -> bool:
        #@ https://www.youtube.com/watch?v=IsvocB5BJhw
        target = sum(nums)
        if target % 2:
            return False
        else:
            target //= 2
        sums = set()
        for n in nums:
            for s in sums.copy():
                sums.add(s + n)
            sums.add(n)
            if target in sums:
                return True
        return False
        
        
        