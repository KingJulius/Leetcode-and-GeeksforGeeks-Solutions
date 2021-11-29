class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        middle = 0
        temp = 0
        
        while start <= end:
            middle = (start+end)//2
            if nums[middle] < target:
                temp = start
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1
            elif nums[middle] == target:
                return middle
        
        #print(start)
        return start