from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        visited = set()
        step = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if (r,c) in visited:
                    continue
                grid[r][c] = step

                visited.add((r,c))
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    if (nr, nc) in visited or grid[nr][nc] != 2147483647:
                        continue
                    q.append((nr, nc))
            
            step += 1