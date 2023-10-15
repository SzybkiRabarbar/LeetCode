# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution: # T: 67.70% M: 40.87%
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        hash = set()
        n = root
        while n:
            hash.add(n)
            if q.val == n.val:
                return n
            elif p.val == n.val:
                break
            elif p.val < n.val:
                n = n.left
            else:
                n = n.right
        n = root
        while n:
            if p.val == n.val:
                return n
            if n in hash:
                res = n
            else:
                break
            if q.val < n.val:
                n = n.left
            else:
                n = n.right
    
        return res