class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { c: [] for c in range(n) }

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def bfs(node):
            q = deque()
            q.append((node, node))
            visited.add(node)
            while q:
                curr, pre = q.popleft()

                for nxt in graph[curr]:
                    if nxt != pre and nxt not in visited:
                        q.append((nxt, curr))
                        visited.add(nxt)
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                bfs(i)
        
        return res