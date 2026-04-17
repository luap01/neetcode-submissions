# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = head

        # 0 1 2
        # 1 = 0.n
        # 0.n = 2
        # 1.n = 0
        # p = 1

        # 1 0 2 3
        # n.n = 1 
        # c.n = n.n
        while curr and curr.next:
            next = curr.next
            curr.next = next.next
            next.next = prev
            prev = next
            
            

        return prev