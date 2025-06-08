/**
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
var equalSubstring = function(s, t, maxCost) {
    let l = 0, currCost = 0, res = 0
    for (let r = 0; r < s.length; r++) {
        currCost += Math.abs(s[r].charCodeAt(0) - t[r].charCodeAt(0))
        while (currCost > maxCost) {
            currCost -= Math.abs(s[l].charCodeAt(0) - t[l].charCodeAt(0))
            l += 1
        }
        res = Math.max(res, r-l+1)
    }
    return res
};