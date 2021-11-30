class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If length of list is 0 or 1
        if len(nums) == 0:
            return 0
        
        prev = 0
        for i in range(1, len(nums)):
            if nums[prev] != nums[i]:
                prev += 1
                nums[prev] = nums[i]

        
        return prev+1