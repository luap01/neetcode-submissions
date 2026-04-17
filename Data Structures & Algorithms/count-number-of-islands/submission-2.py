from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        num_i = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    q = deque()
                    q.append((r,c))
                    num_i += 1
                    while q:
                        i,j = q.popleft()
                        grid[i][j] = "#"

                        for x,y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                            if x < 0 or x >= ROWS or y < 0 or y >= COLS:
                                continue
                            if grid[x][y] == "1":
                                q.append((x,y))

        return num_i