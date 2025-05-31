/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    const smap = {}, tmap = {}

    for (let i = 0; i < s.length; i++) {
        if (!(s[i] in smap)) smap[s[i]] = i
        if (!(t[i] in tmap)) tmap[t[i]] = i
        if (smap[s[i]] !== tmap[t[i]]) return false
    }
    
    return true
};