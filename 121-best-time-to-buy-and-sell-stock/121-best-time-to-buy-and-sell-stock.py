class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, max_sum = 0, 1, 0
        while j < len(prices):
            if prices[i] <= prices[j]:
                max_sum = max(max_sum, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return max_sum