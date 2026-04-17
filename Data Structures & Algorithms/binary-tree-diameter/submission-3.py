# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, node):
        if not node:
            return 0, 0
        
        l_d, l_h = self.rec(node.left)
        r_d, r_h = self.rec(node.right)

        d = max(l_d, r_d, l_h + r_h)
        h = 1 + max(l_h, r_h)
        
        return d, h

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        return self.rec(root)[0]