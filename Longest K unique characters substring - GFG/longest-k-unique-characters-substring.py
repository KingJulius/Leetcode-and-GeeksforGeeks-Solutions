#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        hmap = {}
        i, j = 0, 0
        maxLen = -1
        while j < len(s):
            if s[j] not in hmap:
                hmap[s[j]] = 1
            else:
                hmap[s[j]] += 1
                
            if len(hmap) < k:
                j += 1
            elif len(hmap) == k:
                maxLen = max(maxLen, j-i+1)
                j += 1
            else:
                while k < len(hmap):
                    hmap[s[i]] -= 1
                    if hmap[s[i]] == 0:
                        hmap.pop(s[i])
                    i += 1
                j += 1
        return maxLen

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends