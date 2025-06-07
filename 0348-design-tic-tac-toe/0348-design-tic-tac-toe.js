/**
 * @param {number} n
 */
var TicTacToe = function(n) {
    // [[0, 0], [0, 0], [0, 0]]
    this.countRow = new Array(n).fill(0).map(_ => [0, 0])
    this.countCol = new Array(n).fill(0).map(_ => [0, 0])
    this.countDiag = [[0, 0], [0, 0]]
    this.target = n
};

/** 
 * @param {number} row 
 * @param {number} col 
 * @param {number} player
 * @return {number}
 */
TicTacToe.prototype.move = function(row, col, player) {
    let rowCount = this.countRow[row]
    rowCount[player - 1] += 1
    if (rowCount[player - 1] === this.target) return player

    let colCount = this.countCol[col]
    colCount[player - 1] += 1
    if (colCount[player - 1] === this.target) return player

    let diagCount
    if (row === col) {
        diagCount = this.countDiag[0]
        diagCount[player - 1] += 1
        if (diagCount[player - 1] === this.target) return player
    }
    if (row === this.target - col - 1) {
        diagCount = this.countDiag[1]
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