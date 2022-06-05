class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for __ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return len(word1) + len(word2) - 2*dp[-1][-1]