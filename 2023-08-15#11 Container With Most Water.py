#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int: #T: 93.07% M: 50.56%
        left, right = 0, len(height) - 1
        amount = int()
        while left < right:
            # print(left, right)
            # print((min([height[left], height[right]]) * (right - left)))
            if (min([height[left], height[right]]) * (right - left)) > amount:
                amount = min([height[left], height[right]]) * (right - left)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
            # print()
        return amount

s = Solution()
print(s.maxArea([2,3,4,5,18,17,6]))

