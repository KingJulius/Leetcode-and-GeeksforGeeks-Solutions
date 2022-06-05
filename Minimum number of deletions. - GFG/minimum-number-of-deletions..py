#User function Template for python3
class Solution:
    def minDeletions(self, Str, n): 
        rev_str = Str[::-1]
        dp = [[0 for __ in range(len(rev_str)+1)] for _ in range(len(Str)+1)]
        for i in range(1, len(Str)+1):
            for j in range(1, len(rev_str)+1):
                if Str[i-1] == rev_str[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return len(Str) - dp[-1][-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
       
        N = int(input())
        Str = input().strip()
        ob = Solution()
        ans = ob.minDeletions(Str, N)
        print(ans)
# } Driver Code Ends