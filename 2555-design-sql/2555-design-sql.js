/**
 * @param {string[]} names
 * @param {number[]} columns
 */
var SQL = function(names, columns) {
    this.table = {}
    for (let i = 0; i < names.length; i++) {
        this.table[names[i]] = {
            length: columns[i],
            row: {},
            nextId: 1
        }
    }
};

/** 
 * @param {string} name 
 * @param {string[]} row
 * @return {boolean}
 */
SQL.prototype.ins = function(name, row) {
    if (!(name in this.table) || row.length !== this.table[name].length) return false
    const id = this.table[name].nextId
    this.table[name].row[id] = row
    this.table[name].nextId += 1
    return true
};

/** 
 * @param {string} name 
 * @param {number} rowId
 * @return {void}
 */
SQL.prototype.rmv = function(name, rowId) {
    if (!(name in this.table) || !(rowId in this.table[name].row)) return false
    delete this.table[name].row[rowId]
};

/** 
 * @param {string} name 
 * @param {number} rowId 
 * @param {number} columnId
 * @return {string}
 */
SQL.prototype.sel = function(name, rowId, columnId) {
    if (!(name in this.table) || !(rowId in this.table[name].row)) return "<null>"
    return this.table[name].row[rowId]?.[columnId - 1] ?? "<null>"
};

/** 
 * @param {string} name
 * @return {string[]}
 */
SQL.prototype.exp = function(name) {
    if (!(name in this.table)) return []
    const res = []
    for (let [id, row] of Object.entries(this.table[name].row)) {
        let data = [id, ...row].join(',')
        res.push(data)
    }
    return res
};

/** 
 * Your SQL object will be instantiated and called as such:
 * var obj = new SQL(names, columns)
 * var param_1 = obj.ins(name,row)
 * obj.rmv(name,rowId)
 * var param_3 = obj.sel(name,rowId,columnId)
 * var param_4 = obj.exp(name)
 */