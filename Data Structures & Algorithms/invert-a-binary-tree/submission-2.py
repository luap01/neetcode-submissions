# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def rec(node):
            if not node:
                return
            
            tmp = node.right
            node.right = node.left
            node.left = tmp

            rec(node.right)
            rec(node.left)
            
        rec(root)
        return root