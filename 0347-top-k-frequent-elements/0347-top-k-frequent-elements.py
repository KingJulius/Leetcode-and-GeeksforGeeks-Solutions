class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hmap = defaultdict(int)
        min_heap = []
        res = []
        for num in nums:
            count_hmap[num] += 1
        for key, val in count_hmap.items():
            heappush(min_heap, (val, key))
            if len(min_heap) > k:
                heappop(min_heap)
        while min_heap:
            val, key = heappop(min_heap)
            res.append(key)
        return res