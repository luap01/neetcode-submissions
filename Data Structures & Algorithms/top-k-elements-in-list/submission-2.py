import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nFreq = defaultdict(int)
        
        for num in nums:
            nFreq[num] += 1

        h = []
        for key, val in nFreq.items():
            if len(h) < k:
                heapq.heappush(h, (val, key))
            elif len(h) == k and val > h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, (val, key))
        
        res = []
        while h:
            v, key = heapq.heappop(h)
            res.append(key)
        
        return res