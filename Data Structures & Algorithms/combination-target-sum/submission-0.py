class Solution:
    # procedure backtrack(P, c) is
    # if reject(P, c) then return
    # if accept(P, c) then output(P, c)
    # s ← first(P, c)
    # while s ≠ NULL do
    #    backtrack(P, s)
    #    s ← next(P, s)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res