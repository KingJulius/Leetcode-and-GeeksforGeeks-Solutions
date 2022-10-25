class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Brute Force
        # T.C: O(n^2)
        #res = [-1] * len(arr)
        #for i in range(len(arr)-1):
        #    for j in range(i+1, len(arr)):
        #        if res[i] < arr[j]:
        #            res[i] = arr[j]
        #return res
        
        # O(n)
        maxVal = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(maxVal, arr[i])
            arr[i] = maxVal
            maxVal = newMax
        return arr
        