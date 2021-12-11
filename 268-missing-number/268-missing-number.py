class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for ele in range(len(nums)+1):
            if ele not in nums:
                return ele
        
        return None
        