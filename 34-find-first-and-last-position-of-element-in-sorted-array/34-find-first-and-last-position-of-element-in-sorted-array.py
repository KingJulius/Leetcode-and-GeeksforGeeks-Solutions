class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r  = 0, len(nums)-1
        lpos, rpos = -1, -1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                lpos = m
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        l, r  = 0, len(nums)-1        
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                rpos = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return [lpos, rpos]
        