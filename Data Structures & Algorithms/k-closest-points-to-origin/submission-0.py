class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: 
        # sqrt(x1**2 + y1**2)
        # minHeap
        minHeap = []
        for x1, y1 in points:
            dist = (x1**2 + y1**2)**0.5
            minHeap.append([dist, x1, y1])

        heapq.heapify(minHeap)
        res = []
        while minHeap and len(res) < k:
            dist, x1, y1 = heapq.heappop(minHeap)
            res.append([x1, y1])
        
        return res