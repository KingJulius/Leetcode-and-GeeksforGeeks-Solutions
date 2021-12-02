class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ls = []
        
        for i in range(1,n+1):
            if i%15 == 0 :
                ls.append("FizzBuzz")
            elif i%3 == 0:
                ls.append("Fizz")
            elif i%5 == 0:
                ls.append("Buzz")
            else:
                ls.append(str(i))
        
        return ls