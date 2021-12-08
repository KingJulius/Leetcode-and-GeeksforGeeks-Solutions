class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        nums.sort()
        
        max_count = 0
        max_ele = nums[0]
        
        max_cap = len(nums)//2
        
        count =0
        curr_ele = nums[0]
        
        print(nums)
        for ele in nums:
            #print(curr_ele,'-->',ele)
            if curr_ele == ele:
                count += 1
                curr_e = ele
            else:
                #print(max_count,'--',count ,"...........", max_cap ,'--', count)
                if max_count < count and max_cap <= count:
                    max_count = count
                    max_ele = curr_e
                    
                count = 1
                curr_ele = ele
                
                
        if max_count < count and max_cap <= count:
            max_count = count
            max_ele = ele
            
        return max_ele
        