class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng, min_heap = [], []
        for eff, sp in zip(efficiency, speed):
            eng.append([eff, sp])
        eng.sort(reverse=True)
        speed, res = 0, 0
        for eff, sp in eng:
            if len(min_heap) == k:
                speed -= heappop(min_heap)
            speed += sp
            heappush(min_heap, sp)
            res = max(res, eff*speed)
        return res%(10**9 + 7)
        
        
            