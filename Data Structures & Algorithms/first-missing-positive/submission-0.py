class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_tracker = defaultdict(int)

        for num in nums:
            if num > 0:
                num_tracker[num] += 1
        
        for i in range(1, 2**31-1):
            if num_tracker[i] == 0:
                return i

        return 0