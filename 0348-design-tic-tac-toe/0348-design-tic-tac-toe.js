/**
 * @param {number} n
 */
var TicTacToe = function(n) {
    this.countRows = new Array(n).fill(0).map(_ => [0, 0])
    this.countCols = new Array(n).fill(0).map(_ => [0, 0])
    this.countDiags = [[0, 0], [0, 0]]
    this.target = n
};

/** 
 * @param {number} row 
 * @param {number} col 
 * @param {number} player
 * @return {number}
 */
TicTacToe.prototype.move = function(row, col, player) {
    // Row
    let rowCount = this.countRows[row]
    rowCount[player - 1] += 1
    if (rowCount[player - 1] === this.target) return player

    // Cols
    let colCount = this.countCols[col]
    colCount[player - 1] += 1
    if (colCount[player - 1] === this.target) return player
    
    // Diags
    let diagCount
    if (row === col) {
        diagCount = this.countDiags[0]
        diagCount[player - 1] += 1
        if (diagCount[player - 1] === this.target) return player
    }

    if (row = this.target - 1 - col) {
        diagCount = this.countDiags[1]
        diagCount[player - 1] += 1
        if (diagCount[player - 1] === this.target) return player
    }


    return 0
};

/** 
 * Your TicTacToe object will be instantiated and called as such:
 * var obj = new TicTacToe(n)
 * var param_1 = obj.move(row,col,player)
 */