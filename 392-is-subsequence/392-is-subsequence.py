class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0 for __ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return True if len(s) == dp[-1][-1] else False