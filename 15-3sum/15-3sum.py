class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            lptr , rptr =  i+1 , len(nums) - 1
            while lptr < rptr:
                threeSum = val + nums[lptr] + nums[rptr]
                if threeSum > 0:
                    rptr -= 1
                elif threeSum < 0:
                    lptr += 1
                else:
                    res.append([val, nums[lptr], nums[rptr]])
                    lptr += 1
                    while nums[lptr] == nums[lptr-1] and lptr < rptr:
                        lptr += 1
        
        return res