/**
 * Encodes a list of strings to a single string.
 *
 * @param {string[]} strs
 * @return {string}
 */
var encode = function(strs) {
    let res_str = ''
    for (let i = 0; i < strs.length; i++) {
        res_str += (strs[i].length + '#' + strs[i])
    }
    return res_str
};

/**
 * Decodes a single string to a list of strings.
 *
 * @param {string} s
 * @return {string[]}
 */
var decode = function(s) {
    let res_arr = []
    let i = 0, j = 0
    while (i < s.length) {
        j = i
        while (s[j] !== '#') j++
        let l = parseInt(s.substring(i, j))
        res_arr.push(s.substring(j + 1, j + l + 1))
        i = j + l + 1
    }
    return res_arr
};

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */