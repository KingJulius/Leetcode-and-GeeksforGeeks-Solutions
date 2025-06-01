/**
 * @param {number[]} nums
 * @return {number[]}
 */
var applyOperations = function(nums) {
    // Applying Operations
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] === nums[i+1]) {
            nums[i] *= 2
            nums[i+1] = 0
        }
    }

    // Shifting All 0's to end
    let wptr = 0, temp
    for (let rptr = 0; rptr < nums.length; rptr++) {
        if (nums[rptr]) {
            temp = nums[wptr]
            nums[wptr++] = nums[rptr]
            nums[rptr] = temp
        }
    }

    return nums
};