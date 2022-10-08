class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Monotonically Decreasing Stack
        # Also stores min value to keep track of ith element
        stk = []
        nums_i = nums[0]
        for n in nums[1:]:
            while stk and n >= stk[-1][0]:
                stk.pop()
            if stk and n > stk[-1][1]:
                return True
            stk.append([n, nums_i])
            nums_i = min(nums_i, n)
        return False
            