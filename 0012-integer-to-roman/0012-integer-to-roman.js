/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const romanMap = {
      M: 1000,
      CM: 900,
      D: 500,
      CD: 400,
      C: 100,
      XC: 90,
      L: 50,
      XL: 40,
      X: 10,
      IX: 9,
      V: 5,
      IV: 4,
      I: 1,
    };

    let res = ''

    for (let [key, val] of Object.entries(romanMap)) {
        while (num >= val) {
            num -= val
            res += key
        }
    }

    return res;

};