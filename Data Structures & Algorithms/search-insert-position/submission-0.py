class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # -1 0 2 4 6 8
        # l=0 r=5 m=2
        # l=3 r=5 m=4
        # l=3 r=3 m=3 
        while l < r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return l + 1 if nums[l] < target else l