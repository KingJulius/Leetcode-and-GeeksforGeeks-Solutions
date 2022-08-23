class Solution:
    def trap(self, height: List[int]) -> int:
        #M0: O(n^2) time and O(1) Space
        #M1: O(n) Space and O(n) Time Complexity
        #maxLeft = [0] * len(height)
        #maxRight = [0] * len(height)
        
        #for i in range(1, len(height)):
            #maxLeft[i] = max(maxLeft[i-1], height[i-1])
        
        #for i in range(len(height) - 2,-1,-1):
            #maxRight[i] = max(maxRight[i+1], height[i+1])
        
        #s = 0
        #for i in range(len(height)):
            #s += min(maxLeft[i], maxRight[i]) - height[i] if  0 <= (min(maxLeft[i], maxRight[i]) - height[i]) else 0 
        
        #return s
        
        #M2 O(n) time and O(1) space
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        trappedWater = 0
        while l< r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                trappedWater += (maxLeft - height[l]) if maxLeft - height[l] > 0 else 0
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                trappedWater += (maxRight - height[r]) if maxRight - height[r] > 0 else 0
        return trappedWater
            
        