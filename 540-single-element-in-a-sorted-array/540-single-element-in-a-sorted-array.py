class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 0 1 2 3 4 5 6 7 8
        # 1 1 2 3 3 4 4 8 8
        if len(nums) == 1: return nums[0]
        if len(nums) > 0 and nums[0] != nums[1]: return nums[0] 
        if len(nums) > 0 and nums[-1] != nums[-2]: return nums[-1] 
        l, r = 0, len(nums)-1
        while l<=r:
            m = l + (r-l)//2
            if (nums[m]!=nums[m-1] and nums[m]!=nums[m+1]):
                return nums[m]
            elif (m%2==0 and nums[m]==nums[m+1]) or (m%2!=0 and nums[m]==nums[m-1]):
                l = m + 1
            else:
                r = m - 1

                