class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # only check the first row, first column, last row and last column
        # wherever all 4 have an X we can modify all Os to Xs

        # visited = set()
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


        r = 0
        c = 0
        run_borders = True
        while run_borders:
            print(r,c)
            if board[r][c] == "O":
                dfs(r, c, set())
            if r == 0 and c < len(board[0]) - 1:
                c += 1
            elif c == len(board[0]) - 1 and r < len(board) - 1:
                r += 1
            elif r == len(board) - 1 and c > 0:
                c -= 1
            elif r > 1:
                r -= 1
            else:
                run_borders = False


        print(board)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
