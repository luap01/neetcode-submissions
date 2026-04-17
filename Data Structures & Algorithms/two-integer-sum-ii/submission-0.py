class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum_tracker = {}
        for i, num in enumerate(numbers):
            if num in sum_tracker:
                return [sum_tracker[num]+1, i+1]
            sum_tracker[target - num] = i
        
        return [0, 0]