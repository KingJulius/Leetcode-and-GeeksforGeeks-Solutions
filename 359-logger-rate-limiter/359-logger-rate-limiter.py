class Logger:

    def __init__(self):
        self.hmap = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        shouldPrint = True
        if message not in self.hmap:
            self.hmap[message] = timestamp
        else:
            if self.hmap[message] + 10 <= timestamp:
                self.hmap[message] = timestamp
            else:
                shouldPrint = False
        return shouldPrint


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)