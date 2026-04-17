from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for c, p in prerequisites:
            graph[p].append(c)
            indegree[c] += 1

        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        res = 0
        visited = set()
        while q:
            c = q.popleft()
            nxt = graph[c]
            visited.add(c)

            for n in nxt:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
            
        return len(visited) == numCourses
