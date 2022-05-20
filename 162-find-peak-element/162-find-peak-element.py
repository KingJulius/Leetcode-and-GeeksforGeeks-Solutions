class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if (0 < m and m < len(nums)-1):
                if (nums[m-1] < nums[m] and nums[m+1] < nums[m]):
                    return m
                elif nums[m] < nums[m-1]:
                    r = m - 1
                else:
                    l = m + 1
            elif m == 0:
                if nums[0] < nums[1]:
                    return 1
                else:
                    return 0
            elif m == len(nums)-1:
                if nums[len(nums)-1] < nums[len(nums)-2]:
                    return len(nums)-2
                else:
                    return len(nums)-1
