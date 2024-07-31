class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rptr, wptr = 0, 0
        while rptr < len(nums):
            if nums[rptr] != val:
                nums[wptr] = nums[rptr]
                wptr += 1
            rptr += 1
        return wptr