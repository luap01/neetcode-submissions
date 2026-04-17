class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = {}
        max_len = 0
        curr_len = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c in tracker:
                i = tracker[c]
                tracker = {}
                max_len = max(max_len, curr_len)
                curr_len = 0
                i += 1
            
            tracker[s[i]] = i
            curr_len += 1
            i += 1 
            
        
        max_len = max(max_len, curr_len)

        return max_len