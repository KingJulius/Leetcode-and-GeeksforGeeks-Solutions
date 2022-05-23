class Solution:
    def calcSum(self, num):
        s = 0
        while num:
            s += (num%10)**2
            num //= 10
        return s
    
    def isHappy(self, n: int) -> bool:
        hset = set()
        while n not in hset:
            hset.add(n)
            n = self.calcSum(n)
            if n == 1:
                return True
        return False
        