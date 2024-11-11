/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    // Null & Primiteve Check
    if (obj === null || typeof obj !== 'object')
        return obj;
    
    // Array Check
    if (Array.isArray(obj))
        return obj.filter(Boolean).map(compactObject);
    
    // Object Check
    const compactObj = {};
    for (const key in obj) {
        const value = compactObject(obj[key]);
        if (value)
            compactObj[key] = value;
    }
    return compactObj;
};