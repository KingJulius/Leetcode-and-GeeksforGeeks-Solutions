/**
 * @param {string[]} names
 * @param {number[]} columns
 */
var SQL = function(names, columns) {
    this.table = {}
    for (let i = 0; i < names.length; i++) {
        this.table[names[i]] = {
            colsLength: columns[i],
            rows: {},
            id: 0
        }
    }
};

/** 
 * @param {string} name 
 * @param {string[]} row
 * @return {boolean}
 */
SQL.prototype.ins = function(name, row) {
    if (!(name in this.table) || row.length !== this.table[name].colsLength) return false
    const newId = this.table[name].id + 1
    this.table[name].rows[newId] = row
    this.table[name].id = newId
    return true
};

/** 
 * @param {string} name 
 * @param {number} rowId
 * @return {void}
 */
SQL.prototype.rmv = function(name, rowId) {
    if (!(name in this.table) || !(rowId in this.table[name].rows)) return false
    delete this.table[name].rows[rowId]
};

/** 
 * @param {string} name 
 * @param {number} rowId 
 * @param {number} columnId
 * @return {string}
 */
SQL.prototype.sel = function(name, rowId, columnId) {
    if (!(name in this.table) || !(rowId in this.table[name].rows)) return "<null>"
    return this.table[name].rows[rowId][columnId - 1] ?? '<null>'
};

/** 
 * @param {string} name
 * @return {string[]}
 */
SQL.prototype.exp = function(name) {
    if (!(name in this.table)) return []
    let ex = []
    for (const [id, rows] of Object.entries(this.table[name].rows)) {
        let data = [id, ...rows].join(',')
        ex.push(data)
    }
    return ex
};

/** 
 * Your SQL object will be instantiated and called as such:
 * var obj = new SQL(names, columns)
 * var param_1 = obj.ins(name,row)
 * obj.rmv(name,rowId)
 * var param_3 = obj.sel(name,rowId,columnId)
 * var param_4 = obj.exp(name)
 */