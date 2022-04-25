class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        op = ""
        res = []
        def solve(ip, op):
            if len(ip) == 0:
                res.append(op)
                return
            if not ip[0].isdigit():
                solve(ip[1:], op+ip[0].lower())
                solve(ip[1:], op+ip[0].upper())
            else:
                solve(ip[1:], op+ip[0])
        solve(s, op)
        return res