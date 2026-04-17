class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        tracker = defaultdict(list)
        for i, s in enumerate(strs):
            sorted_s = "".join(sorted(s))
            tracker[sorted_s].append(s)

        for k,v in tracker.items():
            res.append(v)

        return res
                
