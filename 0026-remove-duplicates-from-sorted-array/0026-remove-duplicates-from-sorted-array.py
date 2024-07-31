class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rptr, wptr = 0, 0
        while rptr < len(nums):
            if rptr > 0 and nums[rptr] == nums[rptr-1]:
                rptr += 1
            else:
                nums[wptr] = nums[rptr]
                wptr += 1
                rptr += 1
        return wptr