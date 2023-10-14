# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # M: 33.27% T: 62.53%
    def isBalanced(self, root: TreeNode) -> [int, bool]:
        if not root:
            return True
        l = self.isBalanced(root.left)
        r = self.isBalanced(root.right)
        if not l or not r:
            return False
        if isinstance(l, bool):
            l = 0
        if isinstance(r, bool):
            r = 0
        if not -1 <= l - r <= 1:
            return False
        return l + 1 if l > r else r + 1
            
    
    