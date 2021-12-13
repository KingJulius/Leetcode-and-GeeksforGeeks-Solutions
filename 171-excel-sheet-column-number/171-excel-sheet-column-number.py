class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        val = 0
        
        for i, char in enumerate(columnTitle[::-1]):
            val += pow(26,i) * (ord(char) - 64)
        
        return val