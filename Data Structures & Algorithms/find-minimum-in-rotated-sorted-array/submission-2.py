class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        min_n = float('inf')
        # 5 1 2 3 4

        while l < r:
            m = (l + r) // 2
            # min_n = min(nums[m], min_n)
            if nums[m] <= nums[r]:
                r = m                
            else:
                l = m + 1
        
        return nums[l]