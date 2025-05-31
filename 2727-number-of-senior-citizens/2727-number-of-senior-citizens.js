/**
 * @param {string[]} details
 * @return {number}
 */
var countSeniors = function(details) {
    let numOfSeniors = 0
    let currAge
    for (let i = 0; i < details.length; i++) {
        currAge = details[i].substring(11, 13)
        if (parseInt(currAge) > 60) numOfSeniors += 1
    }
    return numOfSeniors
};