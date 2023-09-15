# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution: # T: 28.64% M: 6.29%
    def __init__(self) -> None:
        self.t = 0
        self.c = 1
        
    def reverseKGroup(self, node: [ListNode, None], k: int) -> ListNode:
        if k == 1: 
            return node
        if node:
            self.t += 1
            if self.t == k:
                self.t = 0
            next = self.reverseKGroup(node.next, k)
        else:
            return None
        
        if self.t:
            self.t -= 1
        elif self.c == 1:
            self.right = next
            self.first = node
            self.c += 1
        elif self.c == k:
            next.next = node
            node.next = self.right
            self.c = 1
            return self.first
        else:
            next.next = node
            self.c += 1
        
        return node

#@ https://youtu.be/1UOPsfP85V4?si=Dv5OFPaAHbg-ATBM
class BetterSolution: # T: 59.96% M: 99.99%
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = groupPrev = ListNode(0, head)
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupPrev.next = kth
            groupNext = kth.next

            # reverse group
            prev, curr = groupNext, head
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            groupPrev = head
            head = groupNext
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
