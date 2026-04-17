from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { c: [] for c in range(n) }

        for c, nb in edges:
            graph[c].append(nb)
            graph[nb].append(c)

        # 3: 4
        # 4: 3
        q = deque()
        visited = set()
        res = 0
        while len(visited) < n:
            res += 1
            if len(visited) < n:
                for nxt in graph.keys():
                    if nxt not in visited:
                        q.append((nxt, nxt))
                        break
            while q:
                c, p = q.popleft()
                if c not in visited:
                    visited.add(c)
                    nbs = graph[c]

                    for nxt in nbs:
                        if nxt != p:
                            q.append((nxt, c))
                    
                    if len(visited) == n:
                        return res
        
        return res
            

