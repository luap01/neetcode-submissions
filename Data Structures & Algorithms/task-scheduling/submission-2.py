from queue import PriorityQueue

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:



        # XXXXXXABCDEF n=1
        # 6
        freqCounter = defaultdict(int)
        for task in tasks:
            freqCounter[task] += 1
        
        h = []
        for k,v in freqCounter.items():
            heapq.heappush(h, (-v, k))

        # XXYY
        # X: 1
        # Y: 2
        res = 0
        popped = []
        while h:
            f, t = heapq.heappop(h)
            f += 1
            freqCounter[t] -= 1
            res += 1
            cd = 0
            if f != 0:
                popped.append((f, t))

            if popped:
                while cd < n and h:
                    f1, t1 = heapq.heappop(h)
                    freqCounter[t1] -= 1
                    f1 += 1
                    if f1 != 0:
                        popped.append((f1, t1))
                    cd += 1
                    res += 1
                while cd < n:
                    res += 1
                    cd += 1
                while popped:
                    heapq.heappush(h, popped.pop())
        
        return res


