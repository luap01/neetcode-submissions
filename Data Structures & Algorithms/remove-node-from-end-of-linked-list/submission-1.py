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

        curr = head
        prev = None
        idx = 0
        while curr:
            if length - idx == n:
                if prev:
                    prev.next = curr.next
                elif curr.next:
                    head = curr.next
                else:
                    return None
                curr = None
                break
            prev = curr
            curr = curr.next
            idx += 1

        return head