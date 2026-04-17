class MaxHeap:
    def __init__(self):
        self.heap = []

    def push_heap(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[(i - 1) // 2] < self.heap[i]:
            self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
            i = (i - 1) // 2
    
    def size(self):
        return len(self.heap)

    def heapify(self):
        i = 0
        # l/r exists
        # larger of the two
        # if <= parent --> stop
        # else swap
        while 2*i+1 < len(self.heap):
            l_c, l_idx = None, 2*i+1
            r_c, r_idx = None, 2*i+2

            child = None
            l_c = self.heap[l_idx]
            r_c = self.heap[r_idx] if r_idx < len(self.heap) else None
            child = r_idx if r_c is not None and r_c > l_c else l_idx

            if self.heap[i] > self.heap[child]:
                break
            else:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
                i = child

    def pop(self):
        val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.heapify()
        return val

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        heap = MaxHeap()
        for stone in stones:
            heap.push_heap(stone)
        
        # simulation 
        while heap.size() > 1:
            y = heap.pop()
            x = heap.pop()
            if x == y:
                continue
            elif x < y:
                y = y - x
                heap.push_heap(y)
        
        return heap.heap[0] if heap.size() > 0 else 0



