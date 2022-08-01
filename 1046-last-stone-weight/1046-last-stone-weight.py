class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for i in range(len(stones)):
            heappush(max_heap, -1*stones[i])
        while len(max_heap) > 1:
            s1 = -1*heappop(max_heap)
            s2 = -1*heappop(max_heap)
            if s1 != s2:
                heappush(max_heap, -1* (max(s1, s2) - min(s1, s2)))
        return -1*max_heap[0] if len(max_heap) == 1 else 0