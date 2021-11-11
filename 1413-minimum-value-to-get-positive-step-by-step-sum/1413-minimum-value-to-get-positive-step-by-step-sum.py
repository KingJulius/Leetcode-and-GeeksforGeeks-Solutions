class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        flag = 0
        sum = 0
        while(flag!=1):
            flag =1
            sum = counter
            for ele in nums:
                sum = sum + ele
                if(sum < 1):
                    counter = counter + 1
                    flag = 0
                    break
   
        return counter
        