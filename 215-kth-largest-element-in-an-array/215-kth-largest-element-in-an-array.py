import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in range(len(nums)):
            heappush(min_heap, nums[i])
            if len(min_heap) > k:
                heappop(min_heap)
        return heappop(min_heap)