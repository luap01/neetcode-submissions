class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        colTracker = { c: set() for c in range(COLS) }
        
        subBoxTracker = {}
        for i in range(1, 4):
            for j in range(1, 4):
                k = (i,j)
                subBoxTracker[k] = set()
        
        # 11 12 13
        # 21 22 23
        # 31 32 33
        
        for r in range(ROWS):
            rowTracker = {}
            i = 1 if r < 3 else 2 if r >= 3 and r < 6 else 3
            for c in range(COLS):
                j = 1 if c < 3 else 2 if c >= 3 and c < 6 else 3
                val = board[r][c]
                if val != ".":
                    if val in rowTracker or val in colTracker[c] or val in subBoxTracker[(i,j)]:
                        return False
                    rowTracker[val] = 1
                    colTracker[c].add(val)
                    subBoxTracker[(i,j)].add(val)
                
        return True

