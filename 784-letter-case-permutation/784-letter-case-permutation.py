class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        op = ""
        res = []
        def solve(ip, op):
            if len(ip) == 0:
                if op not in res:
                    res.append(op)
                return
            if ip[0].isdigit():
                op1 = op+ip[0]
                op2 = op+ip[0]
            else:
                op1 = op+ip[0].lower()
                op2 = op+ip[0].upper()
            solve(ip[1:], op1)
            solve(ip[1:], op2)
            return
        solve(s, op)
        return res