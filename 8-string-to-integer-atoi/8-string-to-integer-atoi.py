class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2**31 -1
        MIN_INT = -2**31
        i = 0
        isPositive = False
        isNegative = False
        res = 0
        
        while i<len(s) and s[i] == " ":
            i += 1
                
        if i < len(s) and s[i] == "+":
            i += 1
            isPositive = True
        
        if i < len(s) and s[i] == "-":
            i += 1
            isNegative = True
        
        if isPositive and isNegative:
            return 0

        while i < len(s) and s[i].isdigit():
            res = 10 * res + int(s[i])
            i += 1
        
        if isNegative and -1*res <= MIN_INT:
            return MIN_INT
        
        if not isNegative and res >= MAX_INT:
            return MAX_INT
        
        return -1 * res if isNegative else res
            
        