#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        i, j, s, max_s = 0, 0, 0, 0
        while j < len(Arr):
            s += Arr[j]
            if j-i+1 == K:
                max_s = max(max_s,s)
                s -= Arr[i]
                i += 1
            j += 1

        
        return max_s

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends