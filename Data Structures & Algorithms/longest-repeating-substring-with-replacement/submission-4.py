class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        
        res = 0
        l = 0
        maxFreq = 0
        # A
        # AA
        # AAA
        # AAAAB
        # 
        for r in range(len(s)):
            count[s[r]] += 1
            maxFreq = max(count[s[r]], maxFreq)

            while r - l + 1 - maxFreq > k:
                count[s[l]] -= 1
                l += 1
                
            
            res = max(res, r - l + 1)
        
        return res


    