from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { c: [] for c in range(n) }

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def bfs(node):
            q = deque()
            q.append(node)
            while q:
                c = q.popleft()
                visited.add(c)
                for nxt in graph[c]:
                    if nxt not in visited:
                        q.append(nxt)

        res = 0
        q = deque()
        for node in graph.keys():
            if node not in visited:
                res += 1
                q.append(node)
                bfs(node)
        
        return res
