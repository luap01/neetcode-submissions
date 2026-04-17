class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        max_a = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q = deque()
                    q.append((r,c))
                    area = 0
                    while q:
                        x, y = q.popleft()
                        grid[x][y] = -1
                        area += 1
                        for nr, nc in [[x+1, y], [x-1, y], [x, y-1], [x, y+1]]:
                            if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                                continue
                            if grid[nr][nc] == 1:
                                grid[nr][nc] = -1
                                q.append((nr, nc))
                    
                    max_a = max(max_a, area)

        return max_a