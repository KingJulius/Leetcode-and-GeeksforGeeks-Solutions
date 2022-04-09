import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        min_heap = []
        
        d = defaultdict(int)
        
        # Dictionary k(val):v(freq)
        for i in range(len(nums)):
            d[nums[i]] += 1
        
        for val, freq in d.items():
            heappush(min_heap, (freq, val))
            if len(min_heap) > k:
                heappop(min_heap)
        
        while min_heap:
            val = heappop(min_heap)
            res.append(val[1])
        
        return res