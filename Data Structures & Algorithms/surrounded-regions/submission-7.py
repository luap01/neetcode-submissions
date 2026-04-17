from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        q = deque()
        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r,0))
            if board[r][COLS - 1]:
                q.append((r,COLS-1))
        
        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0,c))
            if board[ROWS - 1][c]:
                q.append((ROWS-1,c))

        while q:
            r,c = q.popleft()
            if board[r][c] == "O":
                board[r][c] = "#"
                for x,y in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                    if x < ROWS and x > 0 and y < COLS and y > 0:
                        q.append((x,y))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
