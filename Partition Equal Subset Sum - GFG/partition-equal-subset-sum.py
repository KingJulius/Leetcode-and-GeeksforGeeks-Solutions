# User function Template for Python3

class Solution:
    def subsetSum(self, arr, sum):
        res = [[False for j in range(sum+1)] for i in range(len(arr)+1)]
        
        for i in range(len(arr)+1):
            res[i][0] = True
        
        for j in range(1,sum+1):
            res[0][j] = False
            
        for i in range(1,len(arr)+1):
            for j in range(1, sum+1):
                if arr[i-1] <= sum:
                    res[i][j] = res[i-1][j] or res[i-1][j - arr[i-1]]
                else:
                    res[i][j] = res[i-1][j]
        
        return res[len(arr)][sum]    
        
    def equalPartition(self, N, arr):
        # code here
        sum = 0
        for i in range(N):
            sum += arr[i]
            
        if sum%2 != 0:
            return False
        else:
            return self.subsetSum(arr, sum//2)
#{ 
#  Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends