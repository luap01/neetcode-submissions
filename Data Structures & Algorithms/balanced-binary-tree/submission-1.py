# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if not node:
            return 0, True

        l_h, l_b = self.dfs(node.left)
        r_h, r_b = self.dfs(node.right)
        h = 1 + max(l_h, r_h)

        return h, (abs(l_h - r_h) <= 1) and l_b and r_b

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.dfs(root)[1]