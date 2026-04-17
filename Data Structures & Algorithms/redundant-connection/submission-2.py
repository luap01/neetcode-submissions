from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        indegree = [0] * (n + 1)
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            indegree[node] -= 1
            nei = graph[node]
            for nxt in nei:
                indegree[nxt] -= 1
                if indegree[nxt] == 1:
                    q.append(nxt)

        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]

        return [] 