#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        res = [[False for j in range(sum+1)] for i in range(N+1)]
        
        for i in range(N+1):
            res[i][0] = True
        
        for j in range(1, sum+1):
            res[0][j] = False
        
        #print(res)
        
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1] <= j:
                    res[i][j] = res[i-1][j - arr[i-1]] or res[i-1][j]
                else:
                    res[i][j] = res[i-1][j]
        
        return res[N][sum]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends