class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        table = [[0] * (k+1) for _ in range(n+1)]
        for floor in range(1, n+1):
            for egg in range(1, k+1):
                table[floor][egg] += (1 + table[floor-1][egg-1] + table[floor-1][egg] )
                if table[floor][egg] >= n:
                    return floor
        return -1
        
        
        