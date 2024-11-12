/**
 * @param {Object|Array} obj1
 * @param {Object|Array} obj2
 * @return {Object|Array}
 */
function objDiff(obj1, obj2) {
    // 4 cases

    // 1. If both are primitive, then diff
    if (!isObject(obj1) && !isObject(obj2)) {
        return obj1 === obj2 ? {} : [obj1, obj2];
    }
    
    // 2. If one is obj & other is primitive then diff
    if (!isObject(obj1) || !isObject(obj2)) {
        return [obj1, obj2];
    }

    // 3. If one is obj & other is arr then diff
    if (Array.isArray(obj1) !== Array.isArray(obj2)) {
        return [obj1, obj2];
    }

    // 4. If both are arr/objs, then recursion
    const res = {};
    for (const key in obj1) {
        if (obj2.hasOwnProperty(key)) {
            const diff = objDiff(obj1[key], obj2[key]);
            if (Object.keys(diff).length > 0) {
                res[key] = diff;
            }
        }
    }

    return res;

    function isObject(obj) {
        return typeof obj === 'object' && obj !== null;
    }
};