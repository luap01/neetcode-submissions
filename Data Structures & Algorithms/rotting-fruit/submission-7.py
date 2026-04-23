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
        
        minute = 0
        visited = set()
        while q and fresh_fruit > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                visited.add((r,c))
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited:
                        continue
                    
                    if grid[nr][nc] == 1:
                        fresh_fruit -= 1
                        visited.add((nr, nc))
                        q.append((nr, nc))
            minute += 1 
        
        return minute if fresh_fruit <= 0 else -1
