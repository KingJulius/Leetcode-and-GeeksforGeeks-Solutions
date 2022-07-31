class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)-1
        count = 0
        if len(nums) == 0:
            return count
        while l <= r:
            if nums[r] == val:
                count += 1
                r -= 1
            elif nums[l] != val:
                l += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                count += 1
                l += 1
                r -= 1
        return len(nums)-count
            