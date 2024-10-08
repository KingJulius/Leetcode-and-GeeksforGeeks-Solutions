class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        bitMask = 1
        for i in range(32):
            if ((n & bitMask) != 0):
                bits += 1
            bitMask <<= 1
        return bits