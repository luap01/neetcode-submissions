class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        running = nums[0]
        for i in range(1, len(nums)):
            running = running ^ nums[i]

        return running