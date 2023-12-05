# https://leetcode.com/problems/maximum-product-subarray/

class Solution: # T: 76.71% M: 17.69%
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        zeros = [-1] + [i for i, n in enumerate(nums) if not n] + [len(nums)]
        res = -float('inf')
        for i in range(len(zeros) - 1):
            l, r = zeros[i] + 1, zeros[i + 1]
            if not r-l:
                continue
            elif r-l == 1:
                if nums[l] > res: res = nums[l]
                continue
            mult_all = 1
            minus = []
            for j, n in enumerate(nums[l:r], l):
                if n > res:
                    res = n
                if n < 0 and len(minus) == 2:
                        minus[1] = j
                elif n < 0:
                        minus.append(j) 
                mult_all *= n
                
            if mult_all > res: res = mult_all
            
            if mult_all > 0: continue
            
            if len(minus) == 1 or minus[0] == minus[1]:
                left, rigth = 1, 1
                for x in nums[l:minus[0]]:
                    left *= x
                if not minus[0] - l: left = nums[l]
                for x in nums[minus[0]+1:r]:
                    rigth *= x
                if not r - minus[0]+1: rigth = nums[minus[0]]
                res = max(left, rigth, res)
            else:
                mid = 1
                for x in nums[minus[0]+1:minus[1]]:
                    mid *= x
                left = mid
                for x in nums[l:minus[0]+1]:
                    left *= x
                rigth = mid
                for x in nums[minus[1]:r]:
                    rigth *= x
                res = max(left, rigth, res)
        if res < 0 and len(zeros) > 2:
            return 0
        else:
            return res

class Solution: # T: 37.96% M: 38.64%
    #@ https://www.youtube.com/watch?v=lXVy6YWFcRM
    def maxProduct(self, nums: list[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:

            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
