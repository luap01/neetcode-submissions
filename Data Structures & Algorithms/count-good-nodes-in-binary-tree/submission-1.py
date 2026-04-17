# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def compareParent(self, node, max_num):
        if not node:
            return 0
        
        count = 1 if node.val >= max_num else 0
        max_num = max(node.val, max_num)
        
        return count + self.compareParent(node.left, max_num) + self.compareParent(node.right, max_num)

    def goodNodes(self, root: TreeNode) -> int:        

        def dfs(node, max_num):
            if not node:
                return 0

            count = 1 if node.val >= max_num else 0
            max_num = max(node.val, max_num)
            count += dfs(node.left, max_num)
            count += dfs(node.right, max_num)

            return count
        
        return dfs(root, root.val)
        
