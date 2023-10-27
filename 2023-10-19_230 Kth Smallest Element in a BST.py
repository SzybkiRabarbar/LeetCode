# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
        
class Solution: # T: 83.35% M: 70.00%
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        q = deque()
        next_ = root
        while next_:
            q.append(next_)
            next_ = next_.left
        
        i = 0
        while i != k:
            i += 1
            node = q.pop()
            if node.right:
                next_ = node.right
                while next_:
                    q.append(next_)
                    next_ = next_.left
        return node.val