# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, max_val):
            if not node:
                return 0
            
            inc = 0 if node.val < max_val else 1

            max_val = max(node.val, max_val)
            l = dfs(node.left, max_val)
            r = dfs(node.right, max_val)

            return inc + l + r

        return dfs(root, root.val)