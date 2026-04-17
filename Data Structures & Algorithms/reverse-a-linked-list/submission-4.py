# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = curr
        # 1.n = 0
        # 0.n = 2
        # p = 1
        
        # 2.n = 
        # 0.n = 3
        while curr and curr.next:
            next = curr.next
            curr.next = next.next
            next.next = prev
            prev = next
            

        return prev