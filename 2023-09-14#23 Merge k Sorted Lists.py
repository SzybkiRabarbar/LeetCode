# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution: # T: 5.01% M: 98.55% O(k*n)
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        start = ListNode()
        prev = start
        while lists:
            # prev.next = min(lists, key=lambda x: x.val)
            temp = None
            for i, head in enumerate(lists):
                if head and (not temp or temp[1].val > head.val):
                    temp = (i, head)
            if not temp:
                break
            prev.next = temp[1]                   
            prev = prev.next
            lists[temp[0]] = lists[temp[0]].next
        return start.next