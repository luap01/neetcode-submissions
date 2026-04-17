class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        maxHeap = []
        for stone in stones:
            maxHeap.append(-stone)
        
        heapq.heapify(maxHeap)
        # simulation 
        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)
            y, x = -y, -x
            if x == y:
                continue
            elif x < y:
                y = y - x
                heapq.heappush(maxHeap, -y)
        
        return -maxHeap[0] if len(maxHeap) > 0 else 0



