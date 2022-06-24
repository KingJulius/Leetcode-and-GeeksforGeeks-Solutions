class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        visit = set()
        
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                r2, c2 = q.popleft()
                dirs =[[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in dirs:
                    if((r2+dr) in range(rows) and
                      (c2+dc) in range(cols) and
                      grid[r2+dr][c2+dc] == "1" and
                      (r2+dr, c2+dc) not in visit):
                        q.append((r2+dr, c2+dc))
                        visit.add((r2+dr, c2+dc))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    count += 1
        
        return count