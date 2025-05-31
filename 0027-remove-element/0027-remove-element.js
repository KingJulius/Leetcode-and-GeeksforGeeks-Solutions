/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let wptr = 0, rptr = 0
    while (rptr < nums.length) {
        if (nums[rptr] === val) rptr+= 1
        else nums[wptr++] = nums[rptr++]
    }
    return wptr
};