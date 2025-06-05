/**
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
var equalSubstring = function(s, t, maxCost) {
    let maxLen = 0
    let start = 0
    let currCost = 0
    for (let i = 0; i < s.length; i++) {
        currCost += Math.abs(s[i].charCodeAt(0) - t[i].charCodeAt(0))
        while (currCost > maxCost) {
            currCost -= Math.abs(s[start].charCodeAt(0)-t[start].charCodeAt(0))
            start++
        }
        maxLen = Math.max(maxLen, i-start+1)
    }
    return maxLen
};