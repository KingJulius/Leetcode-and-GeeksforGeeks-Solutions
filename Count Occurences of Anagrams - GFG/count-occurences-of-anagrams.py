#User function Template for python3
class Solution:

	
	def search(self,pat, txt):
	    # code here
	    hmap = {}
	    for ele in pat:
	        if ele not in hmap:
	            hmap[ele] = 1
	        else:
	           hmap[ele] += 1
	           
	    i, j, dl_count, count = 0, 0, len(hmap), 0
	    while j < len(txt):
	        if txt[j] in hmap:
	           hmap[txt[j]] -= 1
	           if hmap[txt[j]] == 0:
	               dl_count -= 1
	        if j -i + 1 < len(pat):
	            j += 1
	        elif j - i + 1 == len(pat):
	            if dl_count == 0:
	                count += 1
	            if txt[i] in hmap:
	                hmap[txt[i]] += 1
	                if hmap[txt[i]] == 1:
	                    dl_count += 1
	            i += 1
	            j += 1
	    return count
	                

#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends