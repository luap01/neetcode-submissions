# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        # d = max(height_left + height_r)
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return 0, 0
            
            hL, dL = dfs(node.left)
            hR, dR = dfs(node.right)
            h, d = 1 + max(hL, hR), max(hL + hR, dL, dR)

            return h, d

        return dfs(root)[1]