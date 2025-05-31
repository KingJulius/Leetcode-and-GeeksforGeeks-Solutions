/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false
    
    let hmap = {}
    for (let i = 0; i < s.length; i++) {
        hmap[s[i]] = (hmap[s[i]] || 0) + 1
    }

    for (let i = 0; i < t.length; i++) {
        if (!hmap[t[i]]) return false
        hmap[t[i]] -= 1
    }

    return true
};