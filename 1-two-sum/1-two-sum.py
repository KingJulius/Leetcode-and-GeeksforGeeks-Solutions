class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        id1 = 0
        id2 = 0
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target:
                        id1 = i
                        id2 = j
        
        return id1, id2
        