/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const hmap = {}
    let l = 0, res = 0
    for (let r = 0; r < s.length; r++) {
        hmap[s[r]] = (hmap[s[r]] || 0) + 1
        while (Object.keys(hmap).length < r-l+1) {
            hmap[s[l]] -= 1
            if (hmap[s[l]] === 0) delete hmap[s[l]]
            l += 1
        }
        res = Math.max(res, r-l+1)
    }
    return res
};