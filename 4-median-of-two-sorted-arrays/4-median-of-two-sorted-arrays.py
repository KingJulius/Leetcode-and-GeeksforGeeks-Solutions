import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Assuming the nums1 array is the smaller one
        # If not
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1   
        l = 0
        r = len(nums1) - 1
        total = len(nums1)+len(nums2)
        while True:
            pL = (l+r)//2
            pR = (total)//2 - pL - 2
            minL = nums1[pL] if 0 <= pL else float("-inf")
            maxL = nums1[pL+1] if (pL+1) < len(nums1) else float("inf")
            minR = nums2[pR] if 0 <= pR else float("-inf")
            maxR = nums2[pR+1] if (pR+1) < len(nums2) else float("inf")
            # Left Partition is Correct
            if minL <= maxR and minR <= maxL:
                # For Odd num of elements
                if total%2:
                    return min(maxL, maxR)
                return (max(minL, minR) + min(maxL, maxR)) /2
            elif maxR < minL:
                r = pL - 1
            else:
                l = pL + 1
