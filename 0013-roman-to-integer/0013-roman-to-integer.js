/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    let tSum = map[s[s.length-1]]
    let prev = s[s.length-1]
    for (let i = s.length-2; i >= 0; i--) {
        if (map[s[i]] >= map[prev]) tSum += map[s[i]]
        else tSum -= map[s[i]]
        prev = s[i] 
    }
    return tSum
};