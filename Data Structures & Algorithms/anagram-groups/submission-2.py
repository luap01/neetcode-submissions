class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramTracker = defaultdict(list)

        for s in strs:
            key = "".join(sorted(list(s)))
            anagramTracker[key].append(s)
        
        return list(anagramTracker.values())