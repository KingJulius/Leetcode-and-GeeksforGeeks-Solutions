/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    let nums = [];
    return function curried(...args) {
        nums.push(...args);
        if (fn.length === nums.length){
            const res = fn(...nums);
            return res;
        } else {
            return curried;
        }
    }
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
