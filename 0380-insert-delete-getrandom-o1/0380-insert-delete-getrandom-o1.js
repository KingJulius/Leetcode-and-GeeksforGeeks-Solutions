
var RandomizedSet = function() {
    this.hmap = {}
    this.array = []
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (val in this.hmap) return false
    this.array.push(val)
    this.hmap[val] = this.array.length-1
    return true
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if (!(val in this.hmap)) return false
    let idx = this.hmap[val]
    this.array[idx] = this.array[this.array.length - 1]
    this.hmap[this.array[this.array.length - 1]] = idx
    delete this.hmap[val]
    this.array.pop()
    return true
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    let rId = Math.floor(Math.random() * this.array.length)
    return this.array[rId]
};

/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */