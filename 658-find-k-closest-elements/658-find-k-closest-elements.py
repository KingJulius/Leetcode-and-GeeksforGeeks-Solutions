import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        max_heap = []
        
        for i in range(len(arr)):
            heappush(max_heap, (-1*abs(arr[i] - x), -1*arr[i]))
            if i  >=  k:
                heappop(max_heap)
        
        while max_heap:
            val = heappop(max_heap)
            res.append(-1*val[1])
        
        return sorted(res)