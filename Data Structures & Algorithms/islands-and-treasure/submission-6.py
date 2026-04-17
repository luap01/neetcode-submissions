from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
            
        step = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                grid[r][c] = step
                visited.add((r, c))
                
                for nr, nc in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited:
                        continue

                    if grid[nr][nc] == 2147483647:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            
            step += 1