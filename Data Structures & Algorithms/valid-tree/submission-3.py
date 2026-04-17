from collections import deque 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:    
        graph = { c: [] for c in range(n) }

        for c, nb in edges:
            graph[c].append(nb)
            graph[nb].append(c)
        
        q = deque()
        q.append((0, -1))

        visited = set()
        while q:
            c, p = q.popleft()
            if c in visited:
                return False
            visited.add(c)
            nbs = graph[c]

            for nxt in nbs:
                if nxt != p:
                    q.append((nxt, c))
        
        return len(visited) == n
