/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    let res = 0, num = 0, sign = 1
    const stk = [] 
    for (let c of s) {
        if ('0'.charCodeAt(0) <= c.charCodeAt(0) && c.charCodeAt(0) <= '9'.charCodeAt(0)) {
            num = num * 10 + parseInt(c)
        } else if (c === '+' || c === '-') {
            res += sign * num
            sign = c === '-' ? -1 : 1
            num = 0
        } else if (c === '(') {
            stk.push(res)
            stk.push(sign)
            sign = 1
            res = 0
        } else if (c === ')') {
            res += sign * num
            res *= stk.pop()
            res += stk.pop()
            num = 0
        }
    }
    res += sign * num
    return res
};