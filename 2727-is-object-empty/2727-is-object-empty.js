/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    // Apprach 1 (Can use Object.keys(obj).length as well) O(n) & O(n)
    // if (JSON.stringify(obj).length <= 2){
    //     return true
    // }
    // return false
    
    // Approach 2: O(1) & O(1)
    for(_ in obj){
        return false
    }
    return true
};