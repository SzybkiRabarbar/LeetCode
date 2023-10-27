#https://leetcode.com/problems/3sum/

class Solution:
    
    def threeSum(self, nums: list[int]) -> list[list[int]]: #T: 63.54% M: 88.20%
        results = []
        nums.sort()
        id, left, right = 0, 1, len(nums) - 1
        while nums[id] <= 0:
            if left >= right:
                id += 1
                while id < len(nums) and nums[id] <= nums[id - 1]:
                    id += 1    
                left, right = id+1, len(nums) - 1
                if id >= len(nums):
                    break
                continue
            sum = nums[id] + nums[left] + nums[right]
            if sum > 0:
                right -= 1
                while right > -1 and nums[right] == nums[right + 1]:
                    right -= 1
            elif sum < 0:
                left += 1
                while left < len(nums) and nums[left] == nums[left - 1]:
                    left += 1
            elif sum == 0:
                results.append([nums[id], nums[left], nums[right]])
                left += 1
                while left < len(nums) and nums[left] == nums[left - 1]:
                    left += 1
                right -= 1
                while right > -1 and nums[right] == nums[right + 1]:
                    right -= 1              
        return results
                    

if __name__=="__main__":
    s = Solution()
    x = [-2,0,0,2,2]
    print(s.threeSum(x))