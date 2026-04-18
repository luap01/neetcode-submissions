from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { c : [] for c in range(n) }

        for c, nb in edges:
            graph[c].append(nb)
            graph[nb].append(c)
        
        visited = set()
        res = 0
        q = deque()
        for node in graph.keys():
            if node not in visited:
                res += 1
                q.append((node, node))
                
                while q:
                    c, p = q.popleft()

                    if c not in visited:
                        visited.add(c)
                        nbs = graph[c]

                        for nxt in nbs:
                            if nxt != p:
                                q.append((nxt, c))
        
        return res
