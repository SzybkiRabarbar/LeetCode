# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec: # T: 84.76% M: 79.51%
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ''
        q = deque([root])
        result = f'{root.val} '
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    result += str(node.left.val)
                else:
                    result += 'n'
                result += ' '
                  
                if node.right:
                    q.append(node.right)
                    result += str(node.right.val)
                else:
                    result += 'n'
                result += ' '

        return result
        
    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        rq = None
        lq = deque()
        l, r = 0, 0
        while r < len(data):
            if data[r] == ' ':
                node = TreeNode(int(data[l:r]))
                if rq:
                    rq.right = node
                    rq = None
                elif lq:
                    rq = lq.popleft()
                    rq.left = node
                else:
                    root = node
                lq.append(node)
                l = r + 1
                
            elif data[r] == 'n':
                if rq:
                    rq = None
                elif lq:
                    rq = lq.popleft()
                r += 1
                l = r + 1
            r += 1
        return root
            
        
# Your Codec object will be instantiated and called as such:
ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
ser.deserialize("1 2 3 n n 4 5 n n n n ")