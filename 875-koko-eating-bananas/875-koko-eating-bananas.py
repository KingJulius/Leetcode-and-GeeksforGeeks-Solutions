class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate(k, piles):
            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i]/k)
            return count
        l, r = 1, max(piles)
        minSpeed = r
        while l <= r:
            m = l + (r-l)//2
            hours = calculate(m, piles)
            if hours <= h:
                minSpeed = min(minSpeed, m)
                r = m-1
            else:
                l = m+1
        return minSpeed