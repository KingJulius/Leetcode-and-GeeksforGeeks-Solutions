class Solution:
    def hammingWeight(self, n: int) -> int:
        # Approach 1
        # bits = 0
        # bitMask = 1
        # for i in range(32):
        #     if ((n & bitMask) != 0):
        #         bits += 1
        #     bitMask <<= 1
        # return bits
    
        # Approach 2
        ctr = 0
        while (n != 0):
            n &= (n-1)
            ctr += 1
        return ctr