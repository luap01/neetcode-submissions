# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head

        # find middle
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        curr = slow
        prev = curr
        while curr.next:
            next = curr.next
            curr.next = next.next
            next.next = prev
            prev = next

        # merge two halves
        l1 = head
        l2 = prev
        while l2.next:
            print(l2.val)
            l1_next = l1.next
            l2_next = l2.next
            
            l1.next = l2
            l2.next = l1_next

            l2 = l2_next
            l1 = l1_next 

        return None

            