class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        isNeg = False
        if x < 0:
            isNeg = True
        
        x = abs(x)
        str_result = ""
        
        if isNeg:
            str_result += "-"
        
        while x:
            if (str_result == "" or str_result == "-") and x%10 == 0:
                x /= 10
                continue
            str_result += str(x%10)
            x /= 10
        
        if int(str_result)<=-2147483648 or int(str_result)>=2147483647:
            return 0
        else:
            return int(str_result)
        