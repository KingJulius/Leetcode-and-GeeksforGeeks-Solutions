# User function Template for python3

class Solution:
    def func(self, N, fromm, to, aux):
        if N == 1:
            print("move disk {} from rod {} to rod {}".format(str(1), fromm, to))
            self.counter += 1
            return
        self.func(N-1,fromm,aux,to)
        self.counter += 1
        print("move disk {} from rod {} to rod {}".format(str(N), fromm, to))
        self.func(N-1,aux,to,fromm)
        
    def toh(self, N, fromm, to, aux):
        # Your code here
        self.counter = 0
        self.func(N, fromm, to, aux)
        return self.counter
        
        

#{ 
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends