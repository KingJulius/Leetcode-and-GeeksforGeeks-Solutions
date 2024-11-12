/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || obj === undefined || typeof classFunction !== 'function') {
        return false;
    }
    
    let currObjPropType = Object.getPrototypeOf(obj);
    while (currObjPropType) {
        if (currObjPropType === classFunction.prototype) {
            return true;
        }
        currObjPropType = Object.getPrototypeOf(currObjPropType);
    }
    
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */