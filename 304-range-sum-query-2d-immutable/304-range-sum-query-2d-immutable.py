class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0 for __ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            prefix = 0
            for j in range(1, len(matrix[0])+1):
                prefix += matrix[i-1][j-1]
                self.dp[i][j] = self.dp[i-1][j] + prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        bottomRight = self.dp[r2][c2]
        top = self.dp[r1-1][c2]
        left = self.dp[r2][c1-1]
        topLeft = self.dp[r1-1][c1-1]
        return bottomRight - top - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)