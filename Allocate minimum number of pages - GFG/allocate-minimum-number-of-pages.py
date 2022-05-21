class Solution:
    
    #Function to find minimum number of pages.
    def isValid(self, A, N, M, curr_min):
        numOfStudents = 1
        totSum = 0
        for i in range(N):
            if (A[i] > curr_min):
                return False
            if curr_min < totSum + A[i]:
                numOfStudents += 1
                totSum = A[i]
                if M < numOfStudents:
                    return False
            else:
                totSum += A[i]
        return True
        
    def findPages(self,A, N, M):
        #code here
        res = -1
        if not N < M:
            tsum = 0
            for i in range(len(A)):
                tsum += A[i]
            l, r = 0, tsum
            while l <= r:
                mid = l + (r-l)//2
                if self.isValid(A, N, M, mid):
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
        return res
                


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends