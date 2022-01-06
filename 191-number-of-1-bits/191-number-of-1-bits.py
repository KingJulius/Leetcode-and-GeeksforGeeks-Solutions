class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_num = bin(n)
        str_num = str(bin_num[2:])
        
        while len(str_num) != 32:
            str_num = "0" + str_num
        
        return str_num.count("1")