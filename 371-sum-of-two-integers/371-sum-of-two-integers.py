class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b:
            carry = (a & b)<<1
            a = (a ^ b) & mask
            b = carry & mask
        
        return ~(a^mask) if mask//2 < a else a