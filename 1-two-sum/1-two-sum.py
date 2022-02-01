class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = dict()
        
        for pos, val in enumerate(nums):
            cval = target - val
            if cval not in hmap.keys():
                hmap[val] = pos
            else:
                return [pos, hmap[cval]]