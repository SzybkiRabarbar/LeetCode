# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # T: 92.07% M: 67.25%
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None
        val = max(nums)
        id = nums.index(val)
        return TreeNode(val, self.constructMaximumBinaryTree(nums[:id]), self.constructMaximumBinaryTree(nums[id + 1:]))

    