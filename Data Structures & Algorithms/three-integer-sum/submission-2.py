class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4, -1, 0, 1, 2
        
        nums = sorted(nums)
        l = 0
        res = set()
        for i in range(len(nums) - 1):
            l = i+1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((nums[i], nums[l], nums[r]))
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        
        return list(res)
           