class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        inter_list = []
        
        for ele1 in nums1_set:
            for ele2 in nums2_set:
                if ele1 == ele2:
                    inter_list.append(ele1)
        
        return inter_list