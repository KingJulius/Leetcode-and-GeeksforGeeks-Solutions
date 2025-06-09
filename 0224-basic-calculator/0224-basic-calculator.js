/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    const stk = []
    let res = 0, num = 0, sign = 1
    for (let i = 0; i < s.length; i++) {
        if ('0'.charCodeAt(0) <= s[i].charCodeAt(0) && s[i].charCodeAt(0) <= '9'.charCodeAt(0)) {
            num = 10 * num + parseInt(s[i])
        } else if (s[i] === '+' || s[i] === '-') {
            res += sign * num
            sign = s[i] === '+' ? 1 : -1
            num = 0
        } else if (s[i] === '(') {
            stk.push(res)
            stk.push(sign)
            res = 0
            sign = 1
        } else if (s[i] === ')') {
            res += sign * num
            res *= stk.pop()
            res += stk.pop()
            num = 0
            sign = 1
        }
    }
    res += sign * num
    return res
};