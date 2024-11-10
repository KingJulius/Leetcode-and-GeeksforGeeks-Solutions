/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const res = [];
    const flattening =  (nums, depth) => {
        for (const num of nums){
            if (Array.isArray(num) && depth > 0) {
                flattening(num, depth - 1);
            } else {
                res.push(num);
            }
        }
    };
    flattening(arr, n)
    return res
};