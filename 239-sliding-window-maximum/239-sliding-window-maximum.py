from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        i, j = 0, 0
        
        while j < len(nums):
            while len(queue) > 0  and queue[-1] < nums[j]:
                queue.pop()
            queue.append(nums[j])
            if j - i + 1 < k:
                j += 1
            elif j -i + 1 == k:
                res.append(queue[0])
                if queue[0] == nums[i]:
                    queue.popleft()
                i += 1
                j += 1
        
        return res