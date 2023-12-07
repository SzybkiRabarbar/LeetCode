# https://leetcode.com/problems/all-possible-full-binary-trees/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # T: 65.93% M: 65.61%
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        if n % 2 == 0:
            return []

        hashT = dict()

        def func(n):
            if n in hashT:
                return hashT[n]

            temp = []
            if n == 1:
                temp.append(TreeNode(0))
            else:
                for i in range(1, n - 1, 2):
                    left = func(i)
                    rigth = func(n - i - 1)

                    for l in left:
                        for r in rigth:
                            temp.append(TreeNode(0, l, r))
            hashT[n] = temp
            return temp

        return func(n)