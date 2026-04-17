class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def dfs(i, j, visited):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i,j) in visited:
                return
            
            if board[i][j] == 'X':
                return
            
            visited.add((i,j))
            board[i][j] = '#'
            dfs(i+1, j, visited)
            dfs(i-1, j, visited)
            dfs(i, j+1, visited)
            dfs(i, j-1, visited)


        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0, set())
            if board[r][COLS - 1]:
                dfs(r, COLS - 1, set())
        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c, set())
            if board[ROWS - 1][c]:
                dfs(ROWS - 1, c, set())

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
