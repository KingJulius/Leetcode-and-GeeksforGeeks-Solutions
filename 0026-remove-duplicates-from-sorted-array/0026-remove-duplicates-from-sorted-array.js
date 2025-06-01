/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let rptr = 0, wptr = 0
    while (rptr < nums.length ) {
        if (rptr > 0 && nums[rptr] === nums[rptr-1]) rptr++
        else nums[wptr++] = nums[rptr++]
    }
    return wptr
};