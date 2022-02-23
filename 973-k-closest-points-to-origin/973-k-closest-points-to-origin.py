import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        res = []
                

        for i in range(len(points)):
            heappush(max_heap, (-1*(points[i][0] ** 2 + points[i][1] ** 2), i))
            if i >= k:
                heappop(max_heap)
        
        while max_heap:
            val = heappop(max_heap)
            res.append([points[val[1]][0], points[val[1]][1]])
        
        return res