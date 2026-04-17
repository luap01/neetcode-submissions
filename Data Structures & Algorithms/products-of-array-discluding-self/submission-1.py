class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod = [1] * (len(nums) + 1)
        suf_prod = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            pref_prod[i+1] = pref_prod[i] * nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            suf_prod[i] = suf_prod[i+1] * nums[i]

        res = []
        for i in range(len(nums)):
            res.append(pref_prod[i] * suf_prod[i+1])
        
        return res