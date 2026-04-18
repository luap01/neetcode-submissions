class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = { c: [] for c in range(numCourses) }
        indegree = [0] * numCourses

        for pre, crs in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1

        res = []
        q = deque()
        for pre, crs in queries:
            q.append(pre)
            visited = set()
            while q:
                c = q.popleft()
                if c not in visited:
                    visited.add(c)
                    for nxt in graph[c]:
                        q.append(nxt)
            
            res.append(crs in visited)

        return res