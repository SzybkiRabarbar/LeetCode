# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # T: 46.82% M: 80.68%
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        _ = self.invertTree(root.left)
        _ = self.invertTree(root.right)
        return root