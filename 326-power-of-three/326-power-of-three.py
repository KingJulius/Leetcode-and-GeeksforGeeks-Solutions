import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 0:
            return False
        
        if n == 1:
            return True
        
        count = 1
        
        while True:
            if 3**count < n:
                count += 1
            elif 3**count == n:
                return True
            else:
                return False
        
        return False
   
        