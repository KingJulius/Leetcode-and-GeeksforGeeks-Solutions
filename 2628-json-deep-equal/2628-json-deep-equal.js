/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    // Null Case
    if (o1 === null || o2 === null){
        return o1 === o2;
    }

    // Type Check - makes sure both args are of same types
    if (typeof o1 !== typeof o2){
        return false;
    }

    // Primitive Check
    if (typeof o1 !== 'object'){
        return o1 === o2;
    }

    // Array Check
    if (Array.isArray(o1) || Array.isArray(o2)){
        if (String(o1) !== String(o2)){
            return false;
        }

        for(let i=0; i<o1.length; i++){
            if(!areDeeplyEqual(o1[i], o2[i])){
                return false;
            }
        }
    } else {
        // Object Check
        if(Object.keys(o1).length !== Object.keys(o2).length){
            return false;
        }

        for (const key in o1){
            if (!areDeeplyEqual(o1[key], o2[key])){
                return false;
            }
        }

    }

    return true;
};