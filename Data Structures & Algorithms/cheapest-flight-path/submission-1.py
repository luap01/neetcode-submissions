class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = { c : [] for c in range(n) }
        prices = [float('inf')] * n
        
        for fr, to, pr in flights:
            graph[fr].append([to, pr])

        q = deque([(src, 0)])
        step = 0
        prices[src] = 0
        while q and step <= k:
            for _ in range(len(q)):
                fr, pr = q.popleft()

                for nxt, cst in graph[fr]:
                    if pr + cst < prices[nxt]:
                        prices[nxt] = cst + pr
                        q.append((nxt, prices[nxt]))
            
            step += 1 

        
        return prices[dst] if prices[dst] != float('inf') else -1