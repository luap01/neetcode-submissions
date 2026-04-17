from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        visited = set()
        while q:
            crs = q.popleft()
            nexts = graph[crs]
            visited.add(crs)

            for nxt in nexts:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return len(visited) == numCourses
        