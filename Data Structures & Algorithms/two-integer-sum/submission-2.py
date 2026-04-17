class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumTracker = {}

        # 3 4 5 6
        for i, num in enumerate(nums):
            diff = target - num
            if diff in sumTracker:
                return [sumTracker[diff], i]
            sumTracker[num] = i

        return [0, 0] 