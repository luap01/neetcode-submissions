from collections import deque 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = { c: [] for c in range(n) }

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(crs, pre):
            if crs in visited:
                return False
            
            visited.add(crs)
            for nxt in graph[crs]:
                if nxt == pre:
                    continue
                if not dfs(nxt, crs):
                    return False
            
            return True

        res = dfs(0, -1)
        return res if len(visited) == n else False