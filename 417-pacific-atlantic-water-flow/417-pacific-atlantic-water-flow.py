class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        p_set, a_set = set(), set()
        res = []
        
        def solve(r, c, v_set, prevHt):
            if ((r, c) in v_set or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHt):
                return
            v_set.add((r, c))
            solve(r-1, c, v_set, heights[r][c])
            solve(r+1, c, v_set, heights[r][c])
            solve(r, c-1, v_set, heights[r][c])
            solve(r, c+1, v_set, heights[r][c])
        
        # 1st and last row
        for c in range(COLS):
            solve(0, c, p_set, heights[0][c])
            solve(ROWS-1, c, a_set, heights[ROWS-1][c])
        
        # 1st and last column
        for r in range(ROWS):
            solve(r, 0, p_set, heights[r][0])
            solve(r, COLS-1, a_set, heights[r][COLS-1])
            
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in p_set and (i, j) in a_set:
                    res.append([i, j])
        
        return res