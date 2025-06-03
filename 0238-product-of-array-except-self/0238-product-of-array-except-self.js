/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const res = [1]
    let val = 1

    for(let i = 0; i < nums.length-1; i++){
        val *= nums[i]
        res.push(val)
    }

    val = 1
    for(let i = nums.length-1; i > 0; i--){
        val *= nums[i]
        res[i-1] *= val
    }

    return res
};