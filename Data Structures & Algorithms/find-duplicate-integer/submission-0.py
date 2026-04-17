class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tracker = {}

        for num in nums:
            if num in tracker:
                return num
            else:
                tracker[num] = 1