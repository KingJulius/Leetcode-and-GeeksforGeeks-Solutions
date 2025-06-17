/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    let currSum = 0, res = 0, sign = 1, stk = []
    for (let i = 0; i < s.length; i ++) {
        if ('0'.charCodeAt(0) <= s[i].charCodeAt(0) && s[i].charCodeAt(0) <= '9'.charCodeAt(0)) {
            currSum = 10 * currSum + parseInt(s[i])
        } else if (s[i] === '+' || s[i] === '-') {
            res += sign * currSum
            sign = s[i] === '-' ? -1 : 1
            currSum = 0
        } else if (s[i] === '(') {
            stk.push(res)
            stk.push(sign)
            res = 0
            dir = 1
        } else if (s[i] === ')') {
            res += sign * currSum
            res *= stk.pop()
            res += stk.pop()
            currSum = 0
            dir = 1
        }
    }
    res += sign * currSum
    return res
};