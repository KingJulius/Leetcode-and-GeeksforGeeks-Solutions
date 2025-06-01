/**
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    let incLen = 1, decLen = 1, maxLen = 1
    for (let i = 0; i < nums.length-1; i++) {
        if (nums[i] > nums[i+1]) {
            decLen += 1
            incLen = 1
        } else if (nums[i] < nums[i+1]) {
            incLen += 1
            decLen = 1
        } else {
            incLen = 1
            decLen = 1
        }
        maxLen = Math.max(incLen, decLen, maxLen)
    }

    return maxLen
};