class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = {"+", "-", "*", "/"}
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stk.append(int(tokens[i]))
            else:
                v1 = stk.pop()
                v2 = stk.pop()
                if tokens[i] == "+":
                    stk.append(v1+v2)
                elif tokens[i] == "-":
                    stk.append(v2-v1)
                elif tokens[i] == "*":
                    stk.append(v2*v1)
                else:
                    stk.append(int(v2/v1))
        return stk[0]