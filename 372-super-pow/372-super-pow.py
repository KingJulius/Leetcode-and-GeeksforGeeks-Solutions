class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        s = [str(i) for i in b]
        res = int("".join(s))
        return pow(a, res, 1337)
        