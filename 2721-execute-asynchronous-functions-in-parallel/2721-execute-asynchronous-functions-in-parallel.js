/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise(async(res, rej) => {
        let len = functions.length;
        let ct = 0;
        const result = new Array(len);
        functions.forEach(async(func, idx) => {
            try{
                let val = await func();
                result[idx] = val;
                ct++;
                if (ct === len){
                    res(result);
                }
            } catch (ex) {
                rej(ex);
            }
            
        })
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */