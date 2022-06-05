class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev_s = s[::-1]
        dp = [[0 for __ in range(len(rev_s)+1)] for _ in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(1, len(rev_s)+1):
                if s[i-1] == rev_s[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]