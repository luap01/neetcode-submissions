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

        # reverse second half
        curr = slow
        prev = None
        while curr and curr.next:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev
            prev = nxt

        # merge 2 lists
        l1 = head
        l2 = prev
        while l2:
            l1_n = l1.next
            l2_n = l2.next

            l1.next = l2
            l2.next = l1_n

            l2 = l2_n
            l1 = l1_n