/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === undefined || object === null){
        return String(object)
    }

    // Since Arrays are objects as well, best to check for Array case first
    if (Array.isArray(object)){
        const values = object.map((ele) => jsonStringify(ele));
        return `[${values.join(',')}]`;
    }

    if (typeof object === 'object'){
        const keys = Object.keys(object);
        const keyValuePairs = keys.map((key) => `"${key}":${jsonStringify(object[key])}`)
        return `{${keyValuePairs.join(',')}}`;
    }

    if (typeof object === 'string'){
        return `"${object}"`
    }

    // For Primitives
    return String(object)
};