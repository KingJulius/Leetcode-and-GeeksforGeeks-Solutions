class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += 1
        for k, v in hmap.items():
            if v > len(nums) // 2:
                return k
        return 0