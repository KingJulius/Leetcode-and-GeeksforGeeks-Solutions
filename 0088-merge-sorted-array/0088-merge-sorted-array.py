class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Appraoch 1
#         for i in range(m):
#             nums1[i+m] = nums2[i]
       
#       # T.C: O((n+m)log(n+m)) & S.C: O(1)
#       # Replace with Sorting Algo
#        nums.sort()
        
        # Approach 2: 2 pointers with new array
        # T.C: O(m+n) S.C: O(m+n)
        
        # Approach 3: 2 read pts, 1 write ptr, R to L
        r1p, r2p = m-1, n-1
        for w in range(m+n-1, -1, -1):
            if r2p < 0:
                break
            if r1p >= 0 and nums1[r1p] >= nums2[r2p]:
                nums1[w] = nums1[r1p]
                r1p -= 1
            else:
                nums1[w] = nums2[r2p]
                r2p -= 1