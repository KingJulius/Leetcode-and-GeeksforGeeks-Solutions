class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # M1: Using DP: S.C and T.C : O(n^2)
        #dp = [[float('inf')-1 for __ in range(amount+1)] for _ in range(len(coins)+1)]
        #for i in range(len(coins)+1):
        #    dp[i][0] = 0
        #for i in range(1, len(coins)+1):
        #    for j in range(1, amount+1):
        #        if coins[i-1] <= j:
        #            dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])
        #        else:
        #            dp[i][j] = dp[i-1][j]
        #return dp[-1][-1] if dp[-1][-1] != float('inf')-1 else -1
        
        dp = [float('inf')-1] * (amount+1)
        dp[0] = 0
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[j] = min(dp[j], 1 + dp[j-coins[i-1]])
        return dp[-1] if dp[-1] != float('inf')-1 else -1