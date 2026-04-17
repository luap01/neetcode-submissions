from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            indegree[node] -= 1
            neighbours = graph[node]
            for nxt in neighbours:
                indegree[nxt] -= 1
                if indegree[nxt] == 1:
                    q.append(nxt)

        for a, b in reversed(edges):
            if indegree[a] == 2 and indegree[b]:
                return [a, b]
        
        return []