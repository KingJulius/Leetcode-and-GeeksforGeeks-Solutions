class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1
        for num in nums:
            tmp = currMax * num
            currMax = max(tmp, currMin*num, num)
            currMin = min(tmp, currMin*num, num)
            res = max(currMax, currMin, res)
        return res