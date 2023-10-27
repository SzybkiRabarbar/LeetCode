# https://leetcode.com/problems/diameter-of-binary-tree/

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # T: 79.31% M: 46.03%
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 0
        l = self.recursive(root.left)
        r = self.recursive(root.right)
        if l + r > self.result:
            self.result = l + r
        return self.result
    
    def recursive(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.recursive(root.left)
        r = self.recursive(root.right)
        if l + r > self.result:
            self.result = l + r
        return l + 1 if l >= r else r + 1