# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # length of list
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1

        remove_index = length - n
        if remove_index == 0:
            return head.next

        curr = head
        prev = None        
        idx = 0
        while curr:
            if idx == remove_index:
                if prev:
                    prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            idx += 1

        return head