# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: # T: 43.24% M: 69.30%
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        try:
            self.true_head
        except AttributeError:
            self.true_head = head
        self.num = n
        if head.next:
            _ = self.removeNthFromEnd(head.next, n)
        else:
            return None
        self.num -= 1
        if not self.num:
            head.next = head.next.next
        if self.num == 1 and self.true_head == head:
            return head.next
        return head
        