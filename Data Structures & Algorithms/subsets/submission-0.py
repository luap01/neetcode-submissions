class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, curr):
            if curr in res:
                return
            elif i >= len(nums):
                res.append(curr.copy())

            while i < len(nums):
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
                dfs(i + 1, curr)
                i += 1
        
        dfs(0, [])
        return res
