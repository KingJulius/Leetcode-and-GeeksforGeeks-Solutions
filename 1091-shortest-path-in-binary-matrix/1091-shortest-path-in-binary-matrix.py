class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visitSet = set()
        dirs = [(0, 1), (1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1), (0, -1), (-1, 0)]
        q = deque()
        if grid[0][0] == 0:
            q.append((1, (0, 0)))
            visitSet.add((0, 0))
        while q:
            count, pos = q.popleft()
            if (pos[0], pos[1]) == (len(grid)-1, len(grid[0])-1):
                return count
            for x, y in dirs:
                new_x, new_y = x + pos[0], y + pos[1]
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0 and (new_x, new_y) not in visitSet:
                    q.append((count+1, (new_x, new_y)))
                    visitSet.add((new_x, new_y))
        return -1