/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let cache = {}
    let cval
    for (let i = 0; i < nums.length; i++) {
        cval = target - nums[i]
        if (cval in cache) return [i, cache[cval]]
        cache[nums[i]] = i
    }
    return
};