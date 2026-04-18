from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { c: [] for c in range(numCourses) } 

        for c, pre in prerequisites:
            graph[pre].append(c)
        
        
        def dfs(crs):
            if crs in visited:
                return False
    
            visited.add(crs)
            for nxt in graph[crs]:
                if not dfs(nxt):
                    return False
            
            visited.remove(crs)
            return True

        for c in range(numCourses):
            visited = set()
            if not dfs(c):
                return False
            

        return True