const fs = require('fs')

function solve() {
    let input = fs.readFileSync("/dev/stdin").toString().split("\n");
    let inputIdx = 0

    const TC = parseInt(input[inputIdx++])
    let n = 0, diff = 0

    for (let tc = 0; tc < TC; tc++){
        const [x, y] = input[inputIdx++].split(' ').map(v => +v)
        diff = y - x
        n = Math.ceil((diff ** 0.5) - 1)
        if (n * (n + 1) < diff) console.log(2 * n + 1)
        else console.log(2 * n)
    }
}

solve()
