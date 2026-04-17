class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # track the # of occurences
        # queue ordered by the number of occurences
        # as soon as another occurence we move the element to the front
        # the problem is that the element doesnt have to be the last one
        # we can track the idx of the element in a hashmap
        # however then if we swap with the last element we destroy the order of the queue

        tracker = defaultdict(int)
        for num in nums:
            tracker[num] += 1
        
        # minHeap and only if the element is larger than the minimum element we insert
        minHeap = []
        heapq.heapify(minHeap)
        size = 0
        for key,val in tracker.items():
            if size < k:
                heapq.heappush(minHeap, [val, key])
                size += 1
            else:
                if val > minHeap[0][0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, [val,key])
        
        res = []
        while minHeap:
            val, key = heapq.heappop(minHeap)
            res.append(key)

        return res
