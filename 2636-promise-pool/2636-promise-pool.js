/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
    return new Promise((resolve, reject) => {
        let i = 0;
        let inProgress = 0;

        function callback() {
            if (i === functions.length && inProgress === 0) {
                resolve();
            }

            while (i < functions.length && inProgress < n) {
                functions[i++]()
                    .then(() => {
                        inProgress--;
                        callback();
                    });
                inProgress++;
            }
        }

        callback();
    });
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */