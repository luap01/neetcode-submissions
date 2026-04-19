class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.pref_map = {}
        for r in range(ROWS):
            pref_sum = [0] * (COLS + 1)
            self.pref_map[(r, 0)] = 0
            for c in range(COLS):
                pref_sum[c+1] = matrix[r][c] + pref_sum[c]
                self.pref_map[(r, c + 1)] = pref_sum[c + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_r = 0
        while row1 <= row2:
            sum_r += self.pref_map[(row1, col2 + 1)] - self.pref_map[(row1, col1)]
            row1 += 1
        return sum_r

# 0 3 3 4 8 10
# 0 5 11 14 16 17

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)