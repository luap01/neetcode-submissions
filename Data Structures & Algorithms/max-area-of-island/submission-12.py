class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            
            if grid[r][c] != 1:
                return 0
            
            grid[r][c] = -1

            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        max_a = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_a = max(max_a, dfs(r,c))
        
        return max_a