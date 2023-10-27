#https://leetcode.com/problems/product-of-array-except-self/
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #@OldCodingFarmer
        res = [1] * len(nums)
        for i in range(1, len(nums)): # from left to right 
            res[i] = res[i-1] * nums[i-1]
        tmp = 1
        for i in range(len(nums)-2, -1, -1): # from right to left
            tmp *= nums[i+1]
            res[i] *= tmp
        return res
                
        
if __name__=="__main__":
    nums = [1,2,3,4] # [24,12,8,6]
    t=Solution()
    print(t.productExceptSelf(nums))