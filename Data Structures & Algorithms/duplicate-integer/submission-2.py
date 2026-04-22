class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        for num in nums:
            if num in cache:
                return True
            cache[num] = 1
        return False