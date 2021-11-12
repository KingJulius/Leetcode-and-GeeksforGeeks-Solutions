class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x>0):
            ls = self.createArray(x)
            #print(self.createArray(x))
            i = 0
            j = len(ls)-1
            flag = True
            while(i<=j):
                if ls[i]!=ls[j]:
                    flag = False
                    break
                i = i+1
                j = j-1
        elif(x==0):
            flag = True
        else:
            flag = False
        
        return flag
        
        
    def createArray(self, num):
        ls = []
        while(num!=0):
            val = num%10
            ls.append(val)
            num = num/10
        ls.reverse()
        return ls
        
        