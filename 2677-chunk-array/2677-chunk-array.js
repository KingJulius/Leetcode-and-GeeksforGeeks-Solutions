/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    // Approach 1: T.C:O(n) & S.C: O(1)
    // let res = []
    // let idx = 0
    // while (idx < arr.length){
    //     res.push(arr.slice(idx, idx+size))
    //     idx += size
    // }
    // return res
    
    // Approach 2: T.C:O(n) & S.C: O(1)
    return arr.reduce((chunkedArr, element) => {
        const lastChunk = chunkedArr[chunkedArr.length - 1]
        if (!lastChunk || lastChunk.length === size){
            chunkedArr.push([element])
        } else {
            lastChunk.push(element)
        }
        return chunkedArr
    }, [])
};
