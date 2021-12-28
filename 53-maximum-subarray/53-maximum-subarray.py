class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        currSum = 0
        
        for ele in nums:
            if currSum < 0:
                currSum = 0
            currSum += ele
            maxSum = max(currSum, maxSum)
        
        return maxSum