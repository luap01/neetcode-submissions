class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()

        def dfs(i, j, area):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i,j) in visited:
                return 0

            if grid[i][j] == 0:
                return 0

            visited.add((i, j))
            u = dfs(i+1, j, area)
            d = dfs(i-1, j, area)
            l = dfs(i, j-1, area)
            r = dfs(i, j+1, area)
            
            return 1 + u + d + l + r
        
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c, 0))
        
        return max_area