class MinStack(object):

    def __init__(self):
        self.ls1 = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.ls1.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.ls1.pop()
        return
        
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.ls1):
            return self.ls1[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        val = None
        if len(self.ls1):
            val = self.ls1[0]
            for ele in self.ls1:
                if val > ele:
                    val = ele
        return val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()