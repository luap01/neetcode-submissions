from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    q = deque()
                    q.append((r, c))
                    num_islands += 1 
                    while q:
                        x, y = q.popleft() 
                        grid[x][y] = '#'
                        for nr, nc in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                            if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                                continue
                            if grid[nr][nc] != '1':
                                continue
                            q.append((nr, nc))
        
        return num_islands