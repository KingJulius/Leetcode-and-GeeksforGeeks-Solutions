class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Brute Force
        # T.C: O(n*m)
        # S.C: O(m)
        #hmap = {v:i for i, v in enumerate(nums1)}
        #res = [-1]*len(nums1)
        #for i in range(len(nums2)):
        #    if nums2[i] not in hmap:
        #        continue
        #    for j in range(i+1, len(nums2)):
        #        if nums2[j] > nums2[i]:
        #            idx = hmap[nums2[i]]
        #            res[idx] = nums2[j]
        #            break
        #return res
        
        # Monotonic Increasing Stack
        # T.C: O(m+n)
        # S.C: O(m)
        # n1 = [4, 1, 2]
        # n2 = [2, 1, 0, 3, 4] --> 3 is greatest for 1st 3 elements
        stk = []
        hmap = {v: i for i, v in enumerate(nums1)}
        res = [-1]*len(nums1)
        for i in range(len(nums2)):
            while stk and stk[-1] < nums2[i]:
                idx = stk.pop()
                res[hmap[idx]] = nums2[i]
            if nums2[i] not in hmap:
                continue
            stk.append(nums2[i])
        return res