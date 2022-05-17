#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
        l, r = 0 , n-1
        lpos, rpos = -1, -1
        while l <= r:
            m = l + (r-l)//2
            if arr[m] == x:
                lpos = m
                r = m - 1
            elif arr[m] < x:
                l = m + 1
            else:
                r = m - 1
        l, r = 0 , n-1
        while l <= r:
            m = l + (r-l)//2
            if arr[m] == x:
                rpos = m
                l = m + 1
            elif arr[m] < x:
                l = m + 1
            else:
                r = m - 1
        
        if lpos == -1 and rpos == -1:
            return 0
        elif lpos == rpos:
            return 1
        else:
            return rpos - lpos + 1
#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends