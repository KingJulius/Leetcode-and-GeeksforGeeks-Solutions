class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        min_size, curr_sum = float("inf"), 0
        while j < len(nums):
            curr_sum += nums[j]
            while target <= curr_sum:
                min_size = min(j-i+1, min_size)
                curr_sum -= nums[i]
                i += 1
            j += 1
        return 0 if min_size == float("inf") else min_size
                
        