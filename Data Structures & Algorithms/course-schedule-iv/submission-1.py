class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = { c : list() for c in range(numCourses) }
        indegree = [0] * numCourses

        for pre, crs in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        res = []
        for pre, crs in queries:
            q.append(pre)
            visited = set()
            while q:
                c = q.popleft()
                if c not in visited:
                    visited.add(c)
                    nbs = graph[c]
                    
                    for nxt in nbs:
                        q.append(nxt)
            
            res.append(crs in visited)
    
        return res


        