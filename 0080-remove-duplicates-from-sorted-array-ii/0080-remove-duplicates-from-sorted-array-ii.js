/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length <= 2) {
        return nums.length;
    }
    
    let wptr = 2
    
    for (let rptr = 2; rptr < nums.length ; rptr++) {
        if (nums[rptr] !== nums[wptr-2]){
            nums[wptr++] = nums[rptr];
        }
    }

    return wptr
};