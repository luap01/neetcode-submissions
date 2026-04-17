class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pref_sum = {}
        for i, num in enumerate(nums):
            if num in pref_sum:
                return [pref_sum[num], i]     
            pref_sum[target - num] = i

        return [0,0]