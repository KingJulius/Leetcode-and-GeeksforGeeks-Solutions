
var RandomizedSet = function() {
    this.table = {}
    this.arr = []
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (val in this.table) return false
    this.arr.push(val)
    this.table[val] = this.arr.length - 1
    return true
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if (!(val in this.table)) return false
    let idx = this.table[val]
    this.arr[idx] = this.arr[this.arr.length-1]
    this.table[this.arr[this.arr.length-1]] = idx
    this.arr.pop()
    delete this.table[val]
    return true
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    let rIdx = Math.floor(Math.random()*this.arr.length)
    return this.arr[rIdx]
};

/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */