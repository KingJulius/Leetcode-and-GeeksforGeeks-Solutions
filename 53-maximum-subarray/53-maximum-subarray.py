class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum, curr_sum = nums[0], 0
        for j in range(len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0    
        return max_sum