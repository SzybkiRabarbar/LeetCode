# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # T: 5.23% M 11.53%
    def isValidBST(self, root: TreeNode) -> tuple | bool:
        if root.left:
            l = self.isValidBST(root.left)
        else:
            l = (root.val, root.val - 1)
            
        if root.right:
            r = self.isValidBST(root.right)
        else:
            r = (root.val + 1, root.val)
            
        if not l or not r:
            return False
        elif l[1] >= root.val or r[0] <= root.val:
            return False
        
        return (l[0], r[1])
    
class Solution: # T: 85.82% M: 94.50%
    # @ https://www.youtube.com/watch?v=s6ATEkipzow
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))