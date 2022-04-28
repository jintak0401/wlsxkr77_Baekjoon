const fs = require('fs')

function solve() {
    let input = fs.readFileSync("/dev/stdin").toString().split("\n");

    const TC = parseInt(input[0])

    let ans = 100000000, tx = 0, ty = 0, N = 0
    let x = Array.from({length: 20}, ()=>0)
    let y = Array.from({length: 20}, ()=>0)

    const combi = (cnt, idx, sx, sy) => {
        if (cnt === 0) {
            const tmp = ((tx - 2 * sx) ** 2 + (ty - 2 * sy) ** 2) ** 0.5
            if (tmp < ans) ans = tmp
        }

        else {
            for (let i = idx; i <= N - cnt; i++){
                combi(cnt-1, i+1, sx+x[i], sy+y[i])
            }
        }
    }
    let inputIdx = 1
    for (let tc = 0; tc < TC; tc++){
        N = parseInt(input[inputIdx++])
        ans = 100000000; tx = 0; ty = 0
        for (let i = 0; i < N; i++){
            [x[i], y[i]] = input[inputIdx++].split(' ').map(v => +v)
            tx += x[i]
            ty += y[i]
        }
        combi(Math.floor(N / 2) - 1, 1, x[0], y[0])
        console.log(ans)
    }
}

solve()
