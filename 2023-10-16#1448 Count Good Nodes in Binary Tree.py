# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
        
class Solution: # T: 85.67% M: 50.08%
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, root.val)])
        res = 1
        while q:
            for _ in range(len(q)):
                node, max_ = q.popleft()
                
                if node.left: 
                    if max_ > node.left.val:
                        q.append((node.left, max_))
                    else:
                        q.append((node.left, node.left.val))
                        res += 1
                    
                if node.right: 
                    if max_ > node.right.val:
                        q.append((node.right, max_))
                    else:
                        q.append((node.right, node.right.val))
                        res += 1
        return res