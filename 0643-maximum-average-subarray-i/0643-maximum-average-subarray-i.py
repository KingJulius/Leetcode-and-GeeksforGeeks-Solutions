class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_num, curr = 0, 0
        for i in range(k):
            curr += nums[i]
        max_num = curr
        for i in range(k, len(nums)):
            curr += (nums[i] - nums[i-k])
            max_num = max(max_num, curr)
        return max_num/k