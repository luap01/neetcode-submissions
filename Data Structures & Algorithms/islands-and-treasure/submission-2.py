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
            currStep = {}
            while q:
                i, j = q.popleft()
                currStep[(i, j)] = list()
                for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if x < 0 or x >= ROWS or y < 0 or y >= COLS:
                        continue
                    if grid[x][y] == 2147483647 and (x,y) not in visited:
                        currStep[(i, j)].append((x,y))
                        visited.add((x, y))

            for i, j in currStep.keys():
                grid[i][j] = step
                for x, y in currStep[(i, j)]:
                    q.append((x, y))
            step += 1           
            

