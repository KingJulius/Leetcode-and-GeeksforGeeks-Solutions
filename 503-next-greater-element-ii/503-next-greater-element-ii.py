class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        res = [-1] * len(nums)
        
        for i in range(2):
            for i in range(len(nums)):
                while stk and nums[stk[-1]] < nums[i]:
                    res[stk.pop()] = nums[i]
                stk.append(i) 
        return res