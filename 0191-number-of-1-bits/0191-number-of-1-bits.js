/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    count = 0
    while (n !== 0) {
        count += 1
        n &= (n-1)
    }
    return count
};