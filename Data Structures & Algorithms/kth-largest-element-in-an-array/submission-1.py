class MinHeap:
    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def size(self):
        return len(self.heap)

    def add(self, val):
        if self.size() < self.k or val > self.heap[0]:
            self.push_heap(val)
    
    def push_heap(self, val):
        if self.size() < self.k:
            self.heap.append(val)
            i = self.size() - 1
            while i > 0 and self.heap[(i - 1) // 2] > self.heap[i]:
                self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
                i = (i - 1) // 2
        else:
            self.heap[0] = val
            self.heapify()

    def heapify(self):
        i = 0
        # l/r exists
        # smaller child
        # parent <= child --> stop
        # else swap
        while 2*i+1 < self.size():
            lc, lidx = self.heap[2*i+1], 2*i+1
            ridx = 2*i+2

            child = ridx if ridx < self.size() and self.heap[ridx] < lc else lidx
            if self.heap[i] <= self.heap[child]:
                break
            else:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
                i = child

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap(k, nums)
        return heap.heap[0]
