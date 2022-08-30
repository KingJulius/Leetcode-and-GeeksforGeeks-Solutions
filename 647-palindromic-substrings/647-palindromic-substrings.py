class Solution:
    def countSubstrings(self, s: str) -> int:
        def solve(l, r, count, res):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        count = 0
        res = ''
        for i in range(len(s)):
            count = solve(i, i, count, res)
            count = solve(i, i+1, count, res)
        return count