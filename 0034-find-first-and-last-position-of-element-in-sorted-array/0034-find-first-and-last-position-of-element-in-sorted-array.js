/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    return [binarySearch(nums, target, true), binarySearch(nums, target, false)]
};

function binarySearch(nums, target, isFirstSearch) {
    let l = 0, r = nums.length - 1, m, idx = -1
    while (l<=r) {
        m = Math.floor((r+l)/2)
        if (nums[m] < target) l = m + 1
        else if (target < nums[m]) r = m - 1
        else {
            idx = m
            if (isFirstSearch) r = m - 1
            else l = m + 1
        }
    }
    return idx
}