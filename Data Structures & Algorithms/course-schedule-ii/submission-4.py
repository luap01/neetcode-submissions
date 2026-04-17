from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = { c: list() for c in range(numCourses) }
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] +=1

        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        visited = set()
        res = []
        while q:
            crs = q.popleft()
            visited.add(crs)
            n_c = graph[crs]

            for nxt in n_c:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

            res.append(crs)      

        if len(res) != numCourses:
            return []      
        
        return res