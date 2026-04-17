from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        
        stepTracker = {}
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        step = 0
        to_visit = set()
        while q:
            currentStep = {}
            while q:
                i,j = q.popleft()
                currentStep[(i,j)] = list()
                for x,y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == -1:
                        continue
                    if grid[x][y] == 2147483647 and (x,y) not in to_visit:
                        currentStep[(i,j)].append((x,y))
                        to_visit.add((x,y))

            keys = currentStep.keys()
            for (i,j) in keys:
                grid[i][j] = step
                for (x,y) in currentStep[(i,j)]:
                    q.append((x,y))

            step += 1
        


