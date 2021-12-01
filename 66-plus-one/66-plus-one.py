class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in range(len(digits)-1,-1,-1):
            if digits[-1] >= 0 and digits[-1] < 9 and i == len(digits)-1 :
                digits[i] = digits[i] + 1
            elif digits[-1] == 9 and i == len(digits)-1:
                carry = 1
                digits[-1] = 0
            else:
                sum_1 = digits[i] + carry
                digits[i] = (sum_1)%10
                carry = (sum_1)//10
    
        if carry == 1:
            digits.insert(0, carry)
            
        
        return digits