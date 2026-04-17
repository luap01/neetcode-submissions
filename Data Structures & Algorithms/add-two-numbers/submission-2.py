# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def add(self, l1, l2, carry):
        v = l1.val + l2.val + carry
        carry = 0
        if v > 9:
            v = v % 10
            carry = 1

        return ListNode(v), carry

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        copy_head = None
        prev = None
        while l1 and l2:
            node, carry = self.add(l1, l2, carry)
            if not copy_head:
                copy_head = node
            
            if prev:
                prev.next = node
            
            prev = node 
            l1 = l1.next
            l2 = l2.next

        while l2:
            node, carry = self.add(l2, ListNode(0), carry)
            if not copy_head:
                copy_head = node
            
            if prev:
                prev.next = node
            
            prev = node
            l2 = l2.next

        while l1:
            node, carry = self.add(l1, ListNode(0), carry)
            if not copy_head:
                copy_head = node
            
            if prev:
                prev.next = node
            
            prev = node
            l1 = l1.next

        if carry == 1:
            prev.next = ListNode(1)

        return copy_head