class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        atlantic = set()
        pacific = set()

        def dfs(r, c, visited):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 
            
            if (r,c) in visited:
                return

            visited.add((r, c))
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, visited)
        

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)
        
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)

        return list(atlantic.intersection(pacific))