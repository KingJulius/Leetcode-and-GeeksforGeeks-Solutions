class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        t, b = 0, r-1
        
        while t <= b:
            row = (t+b)//2
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break
        
        if t > b:
            return False
        row = (t+b)//2
        
        i, j = 0, c-1
        while i <= j:
            m = (i+j)//2
            if target > matrix[row][m]:
                i = m + 1
            elif target < matrix[row][m]:
                j = m - 1
            else:
                return True
        
        if i > j:
            return False
        