class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)
        n = len(nums)
        res = set()
        for i in range(0, n):
            for j in range(i + 1, n):
                l = j + 1
                r = n - 1
                while l < r:
                    curr = nums[i] + nums[j] + nums[l] + nums[r]
                    if curr == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif curr < target:
                        l += 1
                    else:
                        r -= 1

        return list(res)