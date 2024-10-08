class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Approach 1: Using Hash Set
        # hset = set(nums)
        # for num in range(len(nums)+1):
        #     if num not in hset:
        #         return num
            
        # Approach 2: XOR
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing