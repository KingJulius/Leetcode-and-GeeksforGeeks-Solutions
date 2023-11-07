# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            r = rand7()
            c = rand7()
            idx = (r-1)*7 + c
            if idx <= 40:
                break
        return (idx-1)%10+1