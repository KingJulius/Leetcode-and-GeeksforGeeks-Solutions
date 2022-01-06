class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        str_bin = bin(n)
        str_bin = str_bin[2:]
        while len(str_bin) != 32:
            str_bin  = "0" + str_bin
            
        rev_str_bin = ""
        for i in range(len(str_bin)-1,-1,-1):
            rev_str_bin += str_bin[i]

        return int(rev_str_bin, 2)