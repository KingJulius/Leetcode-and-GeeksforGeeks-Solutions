/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    // DECLARATIVE SOL
    const fn = (acc, f) => f(acc);
    return function(x) {
        return functions.reduceRight(fn, x);
    }
    // IMPERATIVE SOL
    // return function(x) {
    //     for (let fn of functions.reverse()){
    //         x = fn(x);
    //     }
    //     return x
    // }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */