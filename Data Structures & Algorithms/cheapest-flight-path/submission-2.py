class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = { a : [] for a in range(n) }
        prices = [float('inf')] * n

        for fr, to, pr in flights:
            graph[fr].append((to, pr))

        q = deque()
        q.append((src, 0))
        prices[src] = 0
        stop = 0
        while q and stop <= k:
            for _ in range(len(q)):
                curr, cst = q.popleft()
                for nxt, pr in graph[curr]:
                    if cst + pr < prices[nxt]:
                        prices[nxt] = cst + pr
                        q.append((nxt, cst + pr))

            stop += 1

        return prices[dst] if prices[dst] != float('inf') else -1