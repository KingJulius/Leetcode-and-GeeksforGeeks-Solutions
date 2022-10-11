class FreqStack:

    def __init__(self):
        self.hmap = defaultdict(int)
        self.group = defaultdict(list)
        self.maxCount = 0
        

    def push(self, val: int) -> None:
        self.hmap[val] += 1
        if self.hmap[val] > self.maxCount:
            self.maxCount = self.hmap[val] 
        self.group[self.hmap[val]].append(val)
        

    def pop(self) -> int:
        res = self.group[self.maxCount].pop()
        self.hmap[res] -= 1
        if not self.group[self.maxCount]:
            self.maxCount -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()