# https://leetcode.com/problems/binary-search/

class SolutionWithBulidInFunc: # T: 95.21% M: 66.64%
    def search(self, nums: list[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
        
class Solution: # T: 57.24% M: 30.64%
    def search(self, nums: list[int], target: int) -> int:
        nums = [(id, num) for id, num in enumerate(nums)]
        while nums:
            if nums[len(nums) // 2][1] == target:
                return nums[len(nums) // 2][0]
            elif nums[len(nums) // 2][1] > target:
                nums = nums[:len(nums) // 2]
            else:
                nums = nums[(len(nums) // 2) + 1:]
        return -1
    