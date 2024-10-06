/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    // // Approach 1: JSON.stringify: T.C: O(n) & S.C: O(n)
    // return JSON.stringify(obj).length <= 2

    // // Approach 2: Using Object.keys: T.C: O(n) & S.C: O(n)
    // return Object.keys(obj).length == 0

    // Approach 3:
    for (const _ in obj) return false
    return true
};