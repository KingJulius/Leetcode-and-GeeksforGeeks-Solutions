#User function Template for python3
class Solution:
	def NBitBinary(self, N):
		# code here
        c1, c2 = 0, 0
        res = []
        op = ""
        def solve(op, c1, c2, N):
            if N==0:
                res.append(op)
                return
            solve(op+"1", c1+1, c2, N-1)
            if c2<c1:
                solve(op+"0", c1, c2+1, N-1)
        solve(op, c1, c2, N)
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends