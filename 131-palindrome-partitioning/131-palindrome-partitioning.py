class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True 
        def solve(i):
            if i >= len(s):
                res.append(curr.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    curr.append(s[i:j+1])
                    solve(j+1)
                    curr.pop()
        solve(0)
        return res