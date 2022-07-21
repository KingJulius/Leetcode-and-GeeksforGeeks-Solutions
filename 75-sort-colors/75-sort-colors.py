class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
            return nums
        count = [0] * 3
        for i in range(len(nums)):
            count[nums[i]] += 1
        j = 0
        for i in range(len(nums)):
            while count[j] == 0:
                j += 1
            nums[i] = j
            count[j] -= 1
        return nums
        