class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []
        for i in range(len(candies)):
            res.append(candies[i]+extraCandies >= max_candies)    
        return res