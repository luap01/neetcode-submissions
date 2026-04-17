class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod = [1] * (len(nums) + 1)
        suf_prod = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            pref_prod[i+1] = pref_prod[i] * nums[i]
        
        for i in range(len(nums)-1, 0, -1):
            suf_prod[i] = suf_prod[i+1] * nums[i]

        res = []
        for i in range(len(pref_prod) - 1):
            res.append(pref_prod[i] * suf_prod[i+1])

        return res
        # 1, 1, 2, 8, 48
        # 48, 48, 24, 6, 1
        
        # (pref_sum[i] + suf_sum[i+1]) * len(nums)
        # (suf_sum[i+1] - pref_sum[i]) * len(nums)
        
        # 0, -1, -1, 0, 2, 5
        # 5,  6,  6, 5, 3, 0

        # 
        # -6
        # 

