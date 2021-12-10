class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = {}
        d2 = {}
        output = []
        
        for ele in nums1:
            if ele not in d1.keys():
                d1[ele] = 1
            else:
                d1[ele] += 1
        
        for ele in nums2:
            if ele not in d2.keys():
                d2[ele] = 1
            else:
                d2[ele] += 1
        
        for key, val in d1.items():
            if key in d2.keys():
                count = min(val, d2[key])
                for i in range(count):
                    output.append(key)
        

        return output