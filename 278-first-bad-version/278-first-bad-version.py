# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r, res = 1, n, 0
        while l <= r:
            m = l +(r-l)//2
            if not isBadVersion(m):
                l = m+1
            else:
                res = m
                r = m-1
        return res