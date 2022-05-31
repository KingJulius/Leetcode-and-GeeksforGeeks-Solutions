class Solution:
    def isSubsetSum(self, nums, target):
        dp = [[False for j in range(target + 1)] for i in range(len(nums)+1)]
        
        for i in range(len(nums)):
            dp[i][0] = True
        
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[len(nums)][target]
    
    def canPartition(self, nums: List[int]) -> bool:
        tsum = 0 
        for i in range(len(nums)):
            tsum += nums[i]
        if tsum%2 != 0:
            return False
        else:
            return self.isSubsetSum(nums, tsum//2)