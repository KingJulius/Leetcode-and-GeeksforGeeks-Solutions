import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap = []
        heapify(min_heap)
        for i in range(len(nums)):
            heappush(min_heap, int(nums[i]))
            if len(min_heap) > k:
                heappop(min_heap)
        return str(heappop(min_heap))