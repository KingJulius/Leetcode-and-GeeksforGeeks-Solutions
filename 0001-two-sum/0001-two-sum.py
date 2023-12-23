class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            cval = target - nums[i]
            if cval in hmap:
                return [i, hmap[cval]]
            hmap[nums[i]] = i
        