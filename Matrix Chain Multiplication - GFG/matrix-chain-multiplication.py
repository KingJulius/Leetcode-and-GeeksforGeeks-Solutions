#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        # Recursive Solution
        dp = [[-1 for __ in range(len(arr)+1)] for _ in range(len(arr)+1)]
        def solve(arr, i, j):
            if i >= j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = float("inf")
            for k in range(i, j):
                dp[i][j] = min(solve(arr, i, k) + solve(arr, k+1, j) + arr[i-1]*arr[k]*arr[j], dp[i][j])
            return dp[i][j]
        return solve(arr, 1, len(arr)-1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends