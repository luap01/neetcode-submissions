from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        freshFruit = 0

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    freshFruit += 1

        minutes = 0
        visited = set()
        while q and freshFruit > 0:
            for _ in range(len(q)):
                i,j = q.popleft()
                grid[i][j] = 2
                for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if x < 0 or x >= ROWS or y < 0 or y >= COLS:
                        continue
                    if grid[x][y] == 1 and (x,y) not in visited:
                        q.append((x,y))
                        visited.add((x,y))
                        freshFruit -= 1
                
            minutes += 1

        return minutes if freshFruit <= 0 else -1