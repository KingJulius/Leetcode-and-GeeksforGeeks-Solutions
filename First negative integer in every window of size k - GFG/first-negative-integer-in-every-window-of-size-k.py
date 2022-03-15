#User function Template for python3
from collections import deque
def printFirstNegativeInteger( A, N, K):
    # code here
    queue = deque()
    res = []
    i, j = 0, 0
    while j < N:
        if A[j] < 0:
            queue.append(A[j])
        if j - i + 1 < K:
            j += 1
        elif j - i + 1 == K:
            if len(queue) == 0:
                res.append(0)
            else:
                res.append(queue[0])
                if A[i] == queue[0]:
                    queue.popleft()
            i += 1
            j += 1
    return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends