from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output = []
        q = deque()
        i, j = 0, 0
        while j < len(nums):
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)
            if  i > q[0]:
                q.popleft()
            
            if j - i + 1 == k:
                output.append(nums[q[0]])
                i += 1
            j += 1
        
        return output