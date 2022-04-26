class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # c1 is the counter for the opening brackets
        # c2 is the counter for the closing brackets
        c1, c2 = n, n
        op = ""
        res = []
        def solve(op, c1, c2):
            if c1 == 0 and c2 == 0:
                res.append(op)
                return
            if c1 != 0:
                solve(op+"(", c1-1, c2)
            if c1 < c2:
                solve(op+")", c1, c2-1)
        solve(op, c1, c2)
        return res