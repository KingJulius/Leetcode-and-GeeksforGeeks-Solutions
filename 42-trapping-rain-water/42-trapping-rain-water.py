class Solution:
    def trap(self, height: List[int]) -> int:
        #M1: O(n) Space and O(n) Time Complexity
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        diff = []
        
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        
        for i in range(len(height) - 2,-1,-1):
            maxRight[i] = max(maxRight[i+1], height[i+1])
        
        s = 0
        for i in range(len(height)):
            s += min(maxLeft[i], maxRight[i]) - height[i] if  0 <= (min(maxLeft[i], maxRight[i]) - height[i]) else 0 
        
        return s
