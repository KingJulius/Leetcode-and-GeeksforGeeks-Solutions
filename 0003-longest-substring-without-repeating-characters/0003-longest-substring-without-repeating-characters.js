/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let maxLen = 0
    const hmap = {}
    let l = 0
    for (let r = 0; r < s.length; r++) {
        hmap[s[r]] = (hmap[s[r]] || 0) + 1
        while (r-l+1 > Object.keys(hmap).length) {
            hmap[s[l]] -= 1
            if (hmap[s[l]] === 0) delete hmap[s[l]]
            l++
        }
        maxLen = Math.max(maxLen, r-l+1)
    }
    return maxLen
};