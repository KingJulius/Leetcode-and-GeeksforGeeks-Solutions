import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        min_heap = []
        heapq.heapify(min_heap)
        
        d = {}
        
        # Dictionary k(val):v(freq)
        for i in range(len(nums)):
            if nums[i] not in d.keys():
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        
        i = 0
        for val, freq in d.items():
            heappush(min_heap, (freq, val))
            if i >= k:
                print(heappop(min_heap))
            i += 1

        
        while min_heap:
            val = heappop(min_heap)
            res.append(val[1])
        
        return res