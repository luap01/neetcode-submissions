class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCharFreq = defaultdict(int)
        tCharFreq = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sCharFreq[s[i]] += 1
            tCharFreq[t[i]] += 1

        for k, v in sCharFreq.items():
            if k not in tCharFreq or tCharFreq[k] != v:
                return False
        
        return True