/**
 * @param {number} n
 */
var TicTacToe = function(n) {
    this.rowCount = new Array(n).fill(0).map(_ => [0, 0])
    this.colCount = new Array(n).fill(0).map(_ => [0, 0])
    this.diagCount = [[0, 0], [0, 0]]
    this.target = n
};

/** 
 * @param {number} row 
 * @param {number} col 
 * @param {number} player
 * @return {number}
 */
TicTacToe.prototype.move = function(row, col, player) {
    let rC = this.rowCount[row]
    rC[player - 1] += 1
    if (rC[player - 1] === this.target) return player

    let cC = this.colCount[col]
    cC[player - 1] += 1
    if (cC[player - 1] === this.target) return player

    let dC = this.diagCount
    if (row === col) {
        dC[0][player - 1] += 1
        if (dC[0][player - 1] === this.target) return player
    }

    if (row === this.target - col - 1) {
        dC[1][player - 1] += 1
        if (dC[1][player - 1] === this.target) return player
    }

    return 0
     
};

/** 
 * Your TicTacToe object will be instantiated and called as such:
 * var obj = new TicTacToe(n)
 * var param_1 = obj.move(row,col,player)
 */