class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        while 0 in nums:
            count += 1
            nums.remove(0)
        
        while count > 0:
            nums.append(0)
            count -= 1
            
        