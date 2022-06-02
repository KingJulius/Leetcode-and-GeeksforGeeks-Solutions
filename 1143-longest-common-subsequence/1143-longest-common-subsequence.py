class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Using DP with Memoization (Top Down Approach)
        dp = [[-1 for __ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        def helper(text1, text2, m, n):
            if m == 0 or n == 0:
                return 0
            if not dp[m][n] != -1:
                if text1[m-1] == text2[n-1]:
                    dp[m][n] = 1 + helper(text1, text2, m-1, n-1) 
                else:
                    dp[m][n] = max(helper(text1, text2, m, n-1), helper(text1, text2, m-1, n))
            return dp[m][n]
        return helper(text1, text2, len(text1), len(text2))
        
        # Using DP (Bottom Up Approach)