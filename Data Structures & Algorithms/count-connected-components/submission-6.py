from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { c: [] for c in range(n) }

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(c, p):
            if c in visited:
                return

            visited.add(c)
            for nxt in graph[c]:
                if nxt != p:
                    dfs(nxt, c)
        
        res = 0
        for node in graph.keys():
            if node not in visited:
                res += 1
                dfs(node, -1)
        
        return res
