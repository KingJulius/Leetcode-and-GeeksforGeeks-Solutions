class MedianFinder:

    def __init__(self):
        self.max_heap, self.min_heap = [], []
        

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -1*num)
        # Smaller and Bigger Heap Condition
        if self.max_heap and self.min_heap:
            if -1*self.max_heap[0] > self.min_heap[0]:
                heappush(self.min_heap, -1*heappop(self.max_heap))
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -1*heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, -1*heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-1*self.max_heap[0]+self.min_heap[0])/2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -1*self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()