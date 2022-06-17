class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0 for _ in range(len(nums)+1)]
        for i in range(1, len(self.dp)):
            self.dp[i] = self.dp[i-1] + nums[i-1]
        
        

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right+1] - self.dp[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)