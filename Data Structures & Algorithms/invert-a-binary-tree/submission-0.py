# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rec(self, root):
        if not root:
            return root

        left = self.rec(root.left)
        right = self.rec(root.right)

        root.left = right
        root.right = left

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.rec(root)