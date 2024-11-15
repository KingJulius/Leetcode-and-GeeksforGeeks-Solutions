/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let n1 = 0, n2 = 1;
    let temp;
    while (true) {
        yield n1;
        temp = n1 + n2;
        n1 = n2;
        n2 = temp;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */