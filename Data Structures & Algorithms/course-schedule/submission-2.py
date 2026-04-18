from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { c: [] for c in range(numCourses) } 
        indegree = [0] * numCourses

        for c, pre in prerequisites:
            graph[pre].append(c)
            indegree[c] += 1
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        visited = set()
        while q:
            crs = q.popleft()
            if crs not in visited:
                visited.add(crs)

                for nxt in graph[crs]:
                    indegree[nxt] -= 1 
                    if indegree[nxt] == 0:
                        q.append(nxt)
        
        return len(visited) == numCourses