/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    // Approach 1: S.C: O(1) & T.C: O(n)
    let ctr = 0
    for(let arg of args){
        ctr += 1
    }
    return ctr
    // Approach 2: S.C: O(1) & T.C: O(1)
    return args.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */