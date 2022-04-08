class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res, carry, tSum = "", 0, 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            c1 = int("0b" + a[i], 2) if i < len(a) else 0
            c2 = int("0b" + b[i], 2) if i < len(b) else 0
            tSum = c1 + c2 + carry
            res = str(tSum%2) + res
            carry = tSum//2
        if carry:
            res = str(carry) + res
        return res