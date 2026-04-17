class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tracker = {}

        check = {}
        len_s1 = len(s1)
        for c in s1:
            if c not in tracker:
                tracker[c] = 1
            else:
                tracker[c] += 1

        for i in range(len(s2) - len_s1 + 1):
            sub = s2[i:i+len_s1]
            to_skip = 0
            check = tracker.copy()
            for c in sub:
                if c in tracker:
                    check[c] -= 1
            
            found = True
            for v in check.values():
                if v != 0:
                    found = False
        
            if found:
                return True
            
            i += to_skip
        
        return False

