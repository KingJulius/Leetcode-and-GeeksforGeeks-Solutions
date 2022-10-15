class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Brute Force: O(M*N)
        # Using O(M+N) Solution
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        i, j = 0, COLS-1
        while i < ROWS and j >= 0:
            if grid[i][j] < 0:
                count += ROWS - i
                j -= 1
            else:
                i += 1
        # Using Binary Search SOlution : O(mlogn)
        return count
            