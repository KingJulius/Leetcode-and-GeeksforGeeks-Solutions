class Solution:
    def Util(self, curr, n):
        if n < curr:
            return 0
        elif n == curr:
            return 1
        l = self.Util(curr + 1, n)
        r = self.Util(curr + 2, n)
        return l+r
    
    def climbStairs(self, n: int) -> int:
        #return self.Util(0, n)
        count_ls = [0] * (n+1)
        count_ls[n], count_ls[n-1] = 1, 1
        for i in range(n-2, -1, -1):
            count_ls[i] = count_ls[i+1] + count_ls[i+2]
            
        return count_ls[0]
            