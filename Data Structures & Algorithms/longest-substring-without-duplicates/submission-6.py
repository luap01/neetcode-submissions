class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = {}

        l = 0
        # zxyz
        res = 0
        for r in range(len(s)):
            while s[r] in tracker:
                del tracker[s[l]]
                l += 1
            
            tracker[s[r]] = 1
            res = max(res, r - l + 1)

        return res