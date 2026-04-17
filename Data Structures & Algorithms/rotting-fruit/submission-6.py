from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        fresh_fruit = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_fruit += 1
        
        minutes = 0
        while q and fresh_fruit > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for nr, nc in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_fruit -= 1
                        q.append((nr, nc))

            minutes += 1

        return minutes if fresh_fruit <= 0 else -1