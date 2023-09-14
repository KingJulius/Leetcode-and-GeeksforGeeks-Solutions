class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(0, len(nums)):
            cval  = target - nums[i]
            if cval not in hmap:
                hmap[nums[i]] = i
            else:
                return [i, hmap[cval]]