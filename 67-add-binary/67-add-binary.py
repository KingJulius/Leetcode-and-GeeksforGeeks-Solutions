class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        return bin(int('0b' + a, 2) + int('0b' + b, 2))[2:]