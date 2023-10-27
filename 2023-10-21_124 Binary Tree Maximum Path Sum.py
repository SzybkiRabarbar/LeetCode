# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # T: 91.80% M: 67.58%
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        _ = self.path_sum(root)
        return self.res
    
    def path_sum(self, node: TreeNode) -> int:
        if not node:
            return 0
        
        l = self.path_sum(node.left)
        r = self.path_sum(node.right)
        
        turn_res = l + node.val + r
        if turn_res > self.res:
            self.res = turn_res
            
        result = max([node.val + l, node.val + r, node.val])
        if result > self.res:
            self.res = result
        
        return result