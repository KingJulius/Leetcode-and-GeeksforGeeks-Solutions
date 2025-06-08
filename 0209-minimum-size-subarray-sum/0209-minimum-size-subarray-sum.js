/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let l = 0, res = Infinity, currSum = 0
    for (let r = 0; r < nums.length; r++) {
        currSum += nums[r]
        while (currSum >= target) {
            res = Math.min(res, r-l+1)
            currSum -= nums[l]
            l += 1
        }
    }
    return res === Infinity ? 0 : res
};