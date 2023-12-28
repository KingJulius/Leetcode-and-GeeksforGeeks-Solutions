/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let ctr = 0
    for(let arg of args){
        ctr += 1
    }
    return ctr
    
};

/**
 * argumentsLength(1, 2, 3); // 3
 */