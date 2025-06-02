/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let obj = {}
    for (let i = 0; i < strs.length; i++) {
        let letters = strs[i].split('').sort().join('')
        obj[letters] ? obj[letters].push(strs[i]) : obj[letters] = [strs[i]]    
    }
    return Object.values(obj)
};