class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        counter = 0
        max_counter = 0
        while j < len(nums):
            if nums[j] == 1:
                counter += 1
                j += 1
            elif nums[j] == 0:
                max_counter = max(counter, max_counter)
                counter = 0
                j += 1
                i = j
        
        if counter != 0:
            max_counter = max(counter, max_counter)
            counter = 0
        
        return max_counter
        