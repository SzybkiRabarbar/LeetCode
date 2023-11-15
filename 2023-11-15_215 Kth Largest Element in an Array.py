# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

class Solution: # T: 19.90% M: 47.78%
    """Solution: Heap"""
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            else:
                min_ = heapq.heappop(heap)
                if min_ < n:
                    heapq.heappush(heap, n)
                else:
                    heapq.heappush(heap, min_)
        return heapq.heappop(heap)
    
class Solution: # T: 89.34% M: 97.43%
    """Solution: Sort"""
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return sorted(nums)[len(nums) - k]

class Solution: # DNF 
    """
    @ https://www.youtube.com/watch?v=XEmy13g1Qxc
    Solution: QuickSelect
    Time Complexity:
      - Best Case: O(n)
      - Average Case: O(n)
      - Worst Case: O(n^2)
    Extra Space Complexity: O(1)
    """
    def partition(self, nums: list[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill

    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]