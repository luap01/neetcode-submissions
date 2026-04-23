class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = { c : [] for c in range(numCourses) }
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        visited = set()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        res = []
        while q:
            crs = q.popleft()
            if crs in visited:
                continue
            
            res.append(crs)
            visited.add(crs)
            for nxt in graph[crs]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return res if len(visited) == numCourses else []