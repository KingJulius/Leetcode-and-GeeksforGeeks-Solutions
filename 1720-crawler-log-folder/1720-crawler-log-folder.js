/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
    let folderDepth = 0
    for (let id = 0; id < logs.length; id++){
        if (logs[id] === '../') folderDepth = Math.max(0, folderDepth-1)
        else if (logs[id] !== './') folderDepth += 1
    }
    return folderDepth
};