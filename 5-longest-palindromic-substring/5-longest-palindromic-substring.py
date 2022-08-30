class Solution:
    def longestPalindrome(self, s: str) -> str:
        def solve(l, r, res):
            while l >=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
            return res
        res = ''
        for i in range(len(s)):
            res = solve(i, i, res)
            res = solve(i, i+1, res)
        return res
            