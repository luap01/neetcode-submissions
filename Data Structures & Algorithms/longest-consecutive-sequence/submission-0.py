class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberLookup = {}
        for num in nums:
            numberLookup[num] = 1
        
        # only problem is we have to find start and finish of stored nums
        res = 1 if len(nums) > 0 else 0
        start_seq = []
        for k in numberLookup.keys():
            if k+1 in numberLookup and k-1 not in numberLookup:
                start_seq.append(k)
        
        for k in start_seq:
            noEnd = True
            idx = k
            curr_seq = 0
            while noEnd:
                if idx in numberLookup:
                    curr_seq += 1
                else:
                    noEnd = False
                idx +=1
            
            res = max(res, curr_seq)
        
        return res