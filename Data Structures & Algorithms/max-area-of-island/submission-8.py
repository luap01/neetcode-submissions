class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        indegree = defaultdict(int)

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = 0
                    q = deque()
                    q.append((r,c))
                    # 1 1
                    # 1 1

                    # (0,0) -> (0,1), (1,0)
                    # (0,1) -> (1,0), (1,1)
                    
                    to_visit = set()
                    while q:
                        i, j = q.popleft()
                        grid[i][j] = 0
                        area += 1

                        for x,y in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0 or (x,y) in to_visit:
                                continue
                            else:
                                grid[x][y] = 0
                                q.append((x,y))
                    max_area = max(max_area, area)
        
        return max_area