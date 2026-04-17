# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}

        curr = head
        while curr and curr.next:
            if curr in visited:
                return True
            else:
                visited[curr] = 1
                curr = curr.next
        return False
         