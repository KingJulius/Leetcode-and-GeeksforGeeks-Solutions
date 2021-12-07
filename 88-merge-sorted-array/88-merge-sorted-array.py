class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        #nums1_len = len(nums1)
        
        counter = 0
        
        if n != 0:
            for i in range(len(nums1)-1,-1,-1):
                if counter == n:
                    break
                nums1[i] = nums2[counter]
                counter += 1
        
            nums1.sort()
        
        
    
            