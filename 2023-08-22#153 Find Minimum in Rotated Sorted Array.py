# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution: # T: 70.73% M: 48.77%
    def findMin(self, nums: list[int]) -> int:
        first_el = nums[0]
        left, right = 0, len(nums) - 1 
        while left <= right:
            mid = (right + left) // 2
            if mid and nums[mid] < nums[mid - 1]:
                return nums[mid]      
            elif nums[mid] < first_el:
                right = mid - 1
            else:
                left = mid + 1
        return nums[0]
    
if __name__=="__main__":
    s = Solution()
    print(s.findMin([3,4,5,6,7,0,1,2]))