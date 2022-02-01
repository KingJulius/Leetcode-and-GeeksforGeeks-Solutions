class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        lptr = 0
        rptr = len(nums) - 1
        output = [0] * len(nums)
        counter = len(nums) - 1
        while lptr <= rptr:
            if nums[rptr] ** 2 > nums[lptr] **2:
                output[counter] = nums[rptr] ** 2
                rptr -= 1
            else:
                output[counter] = nums[lptr] ** 2
                lptr += 1
            counter -= 1
        return output
                
            