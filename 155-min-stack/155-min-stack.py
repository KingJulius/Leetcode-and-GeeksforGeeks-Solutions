class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.min_stk):
            self.min_stk.append(min(self.min_stk[-1], val))
        else:
            self.min_stk.append(val)
            

    def pop(self) -> None:
        if len(self.stk):
            self.stk.pop()
            self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1] if len(self.stk) else None

    def getMin(self) -> int:
        return self.min_stk[-1] if len(self.stk) else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()