# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution: # T: 64.95% M: 91.10%
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodes = [ListNode()]
        rest = 0
        while l1 or l2 or rest:
            curr = rest
            if l1:
                curr += l1.val
                l1 = l1.next 
            if l2:
                curr += l2.val
                l2 = l2.next
            rest = curr // 10
            nodes.append(ListNode(curr % 10))
            nodes[-2].next = nodes[-1]
        
        return nodes[1]