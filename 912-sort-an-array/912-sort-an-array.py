class Solution(object):
    def partition(self, nums, start, end):
        rand = random.randint(start,end)
        nums[rand], nums[end] = nums[end], nums[rand]
        pivot = nums[end]
        pindex = start
        for i in range(start, end):
            if nums[i] <= pivot:
                nums[i], nums[pindex] = nums[pindex], nums[i]
                pindex += 1
        nums[end], nums[pindex] = nums[pindex], nums[end]
        return pindex
    
    def quicksort(self, nums, start, end):
        if start < end:
            pind = self.partition(nums, start, end)
            self.quicksort(nums, start, pind-1)
            self.quicksort(nums, pind+1, end)
        return nums
    
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = self.quicksort(nums, 0, len(nums)-1)
        return nums
        