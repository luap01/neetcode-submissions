"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        curr = head
        while curr:
            node = Node(curr.val, None, None)
            nodes[curr] = node
            curr = curr.next

        curr = head
        copy_head = None
        while curr:
            copy_node = nodes[curr]
            copy_node.next = nodes[curr.next] if curr.next else None
            copy_node.random = nodes[curr.random] if curr.random else None
            if not copy_head:
                copy_head = copy_node
            curr = curr.next

        return copy_head
        
            
