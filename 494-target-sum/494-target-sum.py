class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tsum = sum(nums)
        target = abs(target)
        
        if (target+tsum) % 2 or tsum<target:
            return 0
        
        val = (target+tsum)//2
        
        table = [[0 for j in range(val+1)] for i in range(len(nums)+1)]
        
        for i in range(len(nums)+1):
            table[i][0] = 1
        
        for i in range(1, len(nums)+1):
            for j in range(val+1):
                if nums[i-1] <= j:
                    table[i][j] = table[i-1][j-nums[i-1]] + table[i-1][j]
                else:
                    table[i][j] = table[i-1][j]
        
        return table[len(nums)][val]
        
        
        