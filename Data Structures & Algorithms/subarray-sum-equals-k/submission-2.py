class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = curr_sum = 0
        pref_sum = { 0 : 1 }

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            res += pref_sum.get(diff, 0)
            pref_sum[curr_sum] = 1 + pref_sum.get(curr_sum, 0)
        
        return res