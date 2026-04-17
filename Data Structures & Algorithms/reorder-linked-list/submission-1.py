# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        # reverse 2nd half
        curr = slow
        prev = None
        while curr and curr.next:
            next = curr.next
            curr.next = next.next
            next.next = prev
            prev = next

        # merge two lists
        l1 = head
        l2 = prev
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l2 = l2_next
            l1 = l1_next
