/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0, r = nums.length - 1
    let m
    while (l<=r) {
        m = Math.floor((l + r)/2)
        if (nums[m] < target) {
            l = m + 1
        } else if (nums[m] === target) {
            return m
        } else {
            r = m - 1
        }
    }
    return -1
};