# https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: # T: 43.38% M: 18.08%
    def reverseList(self, head: ListNode) -> ListNode:
        temp = None
        new_node = None
        while head:
            new_node = ListNode(val=head.val, next=temp)
            temp = new_node
            head = head.next
        return new_node