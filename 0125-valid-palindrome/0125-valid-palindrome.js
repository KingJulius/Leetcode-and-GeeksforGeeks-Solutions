/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let isAlphanumeric = (c) => {
        return (('a'.charCodeAt(0) <= c.charCodeAt(0)) && (c.charCodeAt(0) <= 'z'.charCodeAt(0)) || ('A'.charCodeAt(0) <= c.charCodeAt(0)) && (c.charCodeAt(0) <= 'Z'.charCodeAt(0)) || ('0'.charCodeAt(0) <= c.charCodeAt(0)) && (c.charCodeAt(0) <= '9'.charCodeAt(0)))
    }
    let i = 0, j = s.length - 1
    while (i < j) {
        if (!isAlphanumeric(s[i])) i++
        else if (!isAlphanumeric(s[j])) j--
        else if (s[i].toLowerCase() !== s[j].toLowerCase()) return false
        else {
            i++
            j--
        }
    }
    return true
};