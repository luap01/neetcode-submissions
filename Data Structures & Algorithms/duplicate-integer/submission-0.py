class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}
        for num in nums:
            if num in tracker:
                return True
            tracker[num] = 1
        return False