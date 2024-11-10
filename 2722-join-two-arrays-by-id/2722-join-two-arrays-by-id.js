/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let i = 0;
    let j = 0;
    const res = [];

    // Sorting Arrays: T.C: O(nlgn)
    const cb = (a, b) => a.id - b.id;
    arr1.sort(cb);
    arr2.sort(cb);

    // 2 ptr approach
    while (i<arr1.length && j<arr2.length) {
        if (arr1[i].id === arr2[j].id){
            res.push({...arr1[i], ...arr2[j]});
            i++;
            j++;
        } else if (arr1[i].id < arr2[j].id) {
            res.push({...arr1[i]});
            i++;
        } else {
            res.push({...arr2[j]});
            j++;
        }
    }

    while (i<arr1.length) {
        res.push({...arr1[i]});
        i++;
    }

    while (j<arr2.length) {
        res.push({...arr2[j]});
        j++;
    }

    // Total T.C: O(nlgn) & S.C: O(1)
    return res
};