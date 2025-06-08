/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    return [binarySearch(nums, target, true), binarySearch(nums, target, false)]
};

function binarySearch(nums, target, findFirst) {
    let l = 0, r = nums.length - 1, idx = -1, mid
    while (l <= r) {
        mid = Math.floor((r-l)/2) + l
        if (nums[mid] < target) l = mid + 1
        else if (target < nums[mid]) r = mid - 1
        else {
            idx = mid
            if (findFirst) r = mid - 1
            else l = mid + 1
        }
    }
    return idx
}