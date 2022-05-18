#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        l, r = 0, n-1
        
        while l <= r:
            m = l + (r-l)//2
            prev = (m + n - 1)%n
            nxt = (m+1)%n
            if arr[m] < arr[prev] and arr[m] < arr[nxt]:
                return m
            elif arr[m] <= arr[r]:
                r = m-1
            elif arr[l] <= arr[m]:
                l = m+1
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends