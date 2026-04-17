class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = defaultdict(int)
        for c in s:
            tracker[c] += 1
        
        for c in t:
            if c in tracker and tracker[c] > 0:
                tracker[c] -= 1
            else:
                return False
            
            if tracker[c] == 0:
                del tracker[c]
        
        return len(tracker) == 0