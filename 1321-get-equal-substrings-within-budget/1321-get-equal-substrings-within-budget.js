/**
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
var equalSubstring = function(s, t, maxCost) {
    let l = 0, currSum = 0, maxLen = 0
    for (let r = 0; r < s.length; r++) {
        let diff = Math.abs(s[r].charCodeAt(0) - t[r].charCodeAt(0))
        currSum += diff
        while (currSum > maxCost) {
            currSum -= Math.abs(s[l].charCodeAt(0) - t[l].charCodeAt(0))
            l += 1
        }
        maxLen = Math.max(maxLen, r-l+1)
    }
    return maxLen
};