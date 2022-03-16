#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        #Complete the function
        mydict = dict()
 
        # Initialize sum and maxLen with 0
        sum = 0
        maxLen = 0
     
        # traverse the given array
        for i in range(n):
     
            # accumulate the sum
            sum += A[i]
     
            # when subArray starts from index '0'
            if (sum == K):
                maxLen = i + 1
     
            # check if 'sum-k' is present in
            # mydict or not
            elif (sum - K) in mydict:
                maxLen = max(maxLen, i - mydict[sum - K])
     
            # if sum is not present in dictionary
            # push it in the dictionary with its index
            if sum not in mydict:
                mydict[sum] = i
     
        return maxLen


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, K = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, K))




# } Driver Code Ends