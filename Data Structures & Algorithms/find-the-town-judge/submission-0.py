class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = { c : [] for c in range(1, n + 1) }
        indegree = [0] * (n+1)

        for a, b in trust:
            graph[a].append(b)
            indegree[b] += 1 
        
        for i in range(1, n+1):
            if indegree[i] == n - 1 and len(graph[i]) == 0:
                return i
        
        return -1

    