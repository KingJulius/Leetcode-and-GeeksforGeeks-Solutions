/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxProfit = 0
    let i = 0, j = 1
    while (j < prices.length) {
        if (prices[i] < prices[j]) maxProfit = Math.max(maxProfit, prices[j]-prices[i])
        else i = j
        j += 1
    }
    return maxProfit
};