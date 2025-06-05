/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let left = 0
    let minLen = Infinity
    let currSum = 0
    for(let right = 0; right < nums.length; right++) {
        currSum += nums[right]
        while (currSum >= target) {
            minLen = Math.min(minLen, right-left+1)
            currSum -= nums[left++]
        }
    }
    return minLen !== Infinity ? minLen : 0
};