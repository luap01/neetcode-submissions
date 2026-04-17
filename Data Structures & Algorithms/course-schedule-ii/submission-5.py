from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1

        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)

        res = []
        while q:
            crs = q.popleft()
            nexts = graph[crs]
            res.append(crs)

            for nxt in nexts:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
            
        if len(res) != numCourses:
            return []
        
        return res