# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution: # T: 40.26% M: 5.04%
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.recursion(head, 0)
        while self.tail:
            front_next = head.next
            back_next = self.tail.next
            head.next = self.tail
            self.tail.next = front_next
            head = front_next
            self.tail = back_next
    
    def recursion(self, node: ListNode, n: int) -> ListNode:
        if node.next:
            n += 1
            t = self.recursion(node.next, n)
        else:
            if n == 1:
                self.tail = None
                return -1
            self.tail = node
            return n // 2 - 1
        if t > 0:
            t -= 1
            node.next.next = node
            node.next = None
            return t
        elif t == 0:
            node.next = None
        return -1