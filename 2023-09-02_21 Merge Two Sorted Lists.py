# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: # M: 87.63% T: 48.60%
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        if list1.val <= list2.val:
            head = list1
            previous = list1
            list1 = list1.next
        else:
            head = list2
            previous = list2
            list2 = list2.next
        
        while list1 and list2:
            if list1.val <= list2.val:
                previous.next = list1
                previous = list1
                list1 = list1.next
            else:
                previous.next = list2
                previous = list2
                list2 = list2.next
        
        if list1:
            previous.next = list1
        elif list2:
            previous.next = list2
        
        return head