from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { c: [] for c in range(n) }

        for c, nb in edges:
            graph[c].append(nb)
            graph[nb].append(c)

        visited = set()
        def dfs(c):
            if c in visited:
                return

            visited.add(c)
            nbs = graph[c]
            for nxt in nbs:
                dfs(nxt)
        
        res = 0
        for node in graph.keys():
            if node not in visited:
                res += 1 
                dfs(node)
        
        return res