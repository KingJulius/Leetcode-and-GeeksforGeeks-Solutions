class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for i in range(len(ops)):
            if ops[i] == "+" and len(res) >= 2:
                res.append(res[-1]+res[-2])
            elif ops[i] == "D" and len(res) >= 1:
                res.append(res[-1]*2)
            elif ops[i] == "C" and len(res) >= 1:
                res.pop()
            else:
                res.append(int(ops[i]))
        return sum(res)
        