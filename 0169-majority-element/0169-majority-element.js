/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let map = {}
    for (let i = 0; i < nums.length; i++) {
        if (!(nums[i] in map)) map[nums[i]] = 0
        map[nums[i]] += 1
    }

    for (let key in map) {
        if (map[key] > Math.floor(nums.length/2)) return parseInt(key)
    }
};