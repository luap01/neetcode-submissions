class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return 0
            
            if grid[i][j] != 1:
                return 0
            
            # if (i,j) in visited:
            #    return 0
            
            grid[i][j] = -1
            # visited.add((i,j))
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area
                

