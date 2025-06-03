/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
  let isIncFlag = true, isDecFlag = true
  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] < nums[i+1]) isDecFlag= false
    if (nums[i] > nums[i+1]) isIncFlag = false
    if (!isDecFlag && !isIncFlag) return false
  }
  return true  
};