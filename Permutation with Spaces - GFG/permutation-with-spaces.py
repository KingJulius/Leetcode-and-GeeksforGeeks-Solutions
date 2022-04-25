#User function Template for python3

class Solution:
    def permutation (self, S):
        # code here
        op = ""
        res = []
        count = 1
        def solve(ip, op):
            if len(ip) == 0:
                res.append(op)
                return
            solve(ip[1:], op+" "+ip[0])
            solve(ip[1:], op+ip[0])
            return
        op = op+S[0]
        S = S[1:]
        solve(S, op)
        return res



#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends