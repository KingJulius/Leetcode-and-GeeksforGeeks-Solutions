/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let l = 0, currSum = 0, minLen = Infinity
    for (let r = 0; r < nums.length; r++) {
        currSum += nums[r]
        while (currSum >= target) {
            minLen = Math.min(minLen, r-l+1)
            currSum -= nums[l]
            l += 1
        }
    }
    return minLen === Infinity ? 0 : minLen
};