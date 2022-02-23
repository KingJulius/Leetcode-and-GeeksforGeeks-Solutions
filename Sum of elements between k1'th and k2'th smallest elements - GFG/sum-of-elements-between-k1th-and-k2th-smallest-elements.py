#User function Template for python3
import heapq
class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        # Your code goes here
        maxheap = []
        for i in range(len(A)):
            heapq.heappush(maxheap, -1*A[i])
            if i >= K1:
                heapq.heappop(maxheap)
        
        k1_ele = -1*maxheap[0]

        maxheap = []
        for i in range(len(A)):
            heapq.heappush(maxheap, -1*A[i])
            if i >= K2:
                heapq.heappop(maxheap)
        
        k2_ele = -1*maxheap[0]

        s = 0
        for i in range(len(A)):
            if k1_ele < A[i] and A[i] < k2_ele:
                s += A[i]
        
        return s
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        sz = [int(x) for x in input().strip().split()]
        k1, k2 = sz[0], sz[1]
        ob=Solution()
        print( ob.sumBetweenTwoKth(a, n, k1, k2) )

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends