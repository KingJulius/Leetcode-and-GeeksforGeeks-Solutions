/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let w = 0, temp
    for (let r = 0; r < nums.length; r++) {
        if (nums[r]) {
            temp = nums[w]
            nums[w++] = nums[r]
            nums[r] = temp
        }
    }
    return nums
};