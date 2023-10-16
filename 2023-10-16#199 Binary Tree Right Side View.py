# https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # T: 44.95% M: 85.40%
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return None
        q = deque([root])
        res = []
        while q:
            res.append(q[-1].val)
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return res