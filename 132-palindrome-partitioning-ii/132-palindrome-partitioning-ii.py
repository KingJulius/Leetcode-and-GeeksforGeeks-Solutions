class Solution:
    def minCut(self, s: str) -> int:
        # Using Recurison
        #def isPalindrome(s, i, j):
        #    while i < j:
        #        if s[i] != s[j]:
        #            return False
        #        else:
        #            i += 1
        #            j -= 1
        #    return True
        #def solve(s, i ,j):
        #    if i >= j:
        #        return 0
        #    res = float('inf')
        #    if isPalindrome(s, i, j):
        #        return 0
        #    for k in range(i, j):
        #        res = min(solve(s, i, k) + solve(s, k+1, j) + 1, res)
        #    return res
        #return solve(s, 0, len(s)-1)
        # Using DP: Bottom Up Approach: O(n^2)
        dp = [[-1 for _ in range(len(s)+1)] for __ in range(len(s)+1)]
        def ispal(s):
            if(s==s[::-1]):
                return True
            else:
                return False

        def solve(s,i,j,dp):
            if(i>=j):
                return 0
            if ispal(s[i:j+1]):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            min_step=float('inf')
            for k in range(i,j):
                if(ispal(s[i:k+1])):
                    min_step=min(min_step,1+solve(s,k+1,j,dp))
            dp[i][j]=min_step
            return dp[i][j]

        dp=[[-1 for j in range(len(s))]for i in range(len(s))]
        return solve(s,0,len(s)-1,dp)
        