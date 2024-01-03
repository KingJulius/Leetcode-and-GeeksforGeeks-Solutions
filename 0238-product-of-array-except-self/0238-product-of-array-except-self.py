class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        larr = [1]
        rarr = [1]
        val = 1
        for i in range(len(nums)-1):
            val *= nums[i]
            larr.append(val)
        print(larr)
        val = 1
        for i in range(len(nums)-1, 0, -1):
            val *= nums[i]
            rarr.insert(0, val)
        print(rarr)
        for i in range(len(nums)):
            nums[i] = larr[i] * rarr[i]
        return nums