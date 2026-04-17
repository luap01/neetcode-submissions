class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k or val > self.heap[0]:
            self.push_heap(val)
        return self.heap[0] 

    def push_heap(self, val):
        if len(self.heap) < self.k:
            self.heap.append(val)
            self.sift_up(len(self.heap) - 1)
        else:
            self.heap[0] = val
            self.sift_down(0)
    

    def sift_up(self, i):
        while i > 0 and self.heap[(i - 1) // 2] > self.heap[i]:
            self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
            i = (i - 1) // 2

    def sift_down(self, i):
        # l/r exist
        # smaller child
        # if parent <= child --> stop
        # else swap and continue

        while 2 * i + 1 < len(self.heap) or 2 * i + 2 < len(self.heap):
            l_c = None
            r_c = None
            l_idx = 2*i+1
            r_idx = 2*i+2
            if l_idx < len(self.heap):
                l_c = self.heap[l_idx]
            if r_idx < len(self.heap):
                r_c = self.heap[r_idx]
            
            child = None
            if l_c is not None and r_c is not None:
                child = l_idx if l_c < r_c else r_idx
            elif l_c is not None:
                child = l_idx
            else:
                child = r_idx
            
            if self.heap[i] <= self.heap[child]:
                break
            else:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
                i = child

# parent      = (i - 1) // 2
# left child  = 2*i + 1
# right child = 2*i + 2