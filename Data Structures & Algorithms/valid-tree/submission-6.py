from collections import deque 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = { c: [] for c in range(n) }

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        q = deque()
        q.append((0, -1))
        while q:
            c, p = q.popleft()

            if c not in visited:
                visited.add(c)

                for nxt in graph[c]:
                    if nxt != p:
                        q.append((nxt, c))
            else:
                return False
        
        return len(visited) == n