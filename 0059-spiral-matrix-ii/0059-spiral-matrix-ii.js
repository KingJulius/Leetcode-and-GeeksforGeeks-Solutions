/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
    let l = 0, r = n - 1, t = 0, b = n - 1;
    let ctr = 1;
    let mat = Array.from({length : n}, () => Array(n).fill(0));
    while (l<=r && t <=b) {
        for(let i=l; i<=r; i++) mat[t][i] = ctr++;
        t++;
        for(let i=t; i<=b; i++) mat[i][r] = ctr++;
        r--;
        for(let i=r; i>=l; i--) mat[b][i] = ctr++;
        b--;
        for(let i=b; i>=t; i--) mat[i][l] = ctr++;
        l++;
    }
    return mat;
};