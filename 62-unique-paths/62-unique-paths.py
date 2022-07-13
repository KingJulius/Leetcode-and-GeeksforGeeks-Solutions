class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(n+1) ] for __ in range(m+1)]
        matrix[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
        return matrix[0][0]