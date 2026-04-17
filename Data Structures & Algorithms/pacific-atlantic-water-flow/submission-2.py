class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        atlantic = set()
        pacific = set()

        def dfs(r, c, visited):
            if (r,c) in visited:
                return

            visited.add((r,c))
            for nr, nc in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
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
            