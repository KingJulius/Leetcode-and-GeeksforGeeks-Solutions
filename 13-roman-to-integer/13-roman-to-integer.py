class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        prev = 0
        for i in range(len(s)-1, -1, -1):
            if symbols[s[i]] >= prev:
                sum += symbols[s[i]]
            else:
                sum -= symbols[s[i]]
            prev = symbols[s[i]]
        return sum