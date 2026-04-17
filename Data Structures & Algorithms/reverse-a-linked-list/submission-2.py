# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        
        while head and head.next:
            next = head.next
            head.next = next.next
            next.next = prev
            prev = next
        
        return prev