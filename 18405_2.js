const fs = require('fs');

const d = [[0, 1], [1, 0], [0, -1], [-1, 0]];

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');
    let inputIdx = 0;
    const [N, K] = input[inputIdx++].split(' ').map(Number);
    const arr = Array.from({length: N}, () => input[inputIdx++].split(' ').map(Number));
    const [S, X, Y] = input[inputIdx++].split(' ').map(Number);
    const virusPos = Array.from({length: K + 1}, () => []);
    let flag;

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (arr[i][j] > 0) virusPos[arr[i][j]].push([i, j]);
        }
    }

    for (let s = 0; s < S; s++) {
        flag = false;
        for (let k = 1; k <= K; k++) {
            let newPos = [];
            for (const [ox, oy] of virusPos[k]) {
                for (const [dx, dy] of d) {
                    const x = ox + dx, y = oy + dy;
                    if (arr[x]?.[y] === 0) {
                        arr[x][y] = k;
                        newPos.push([x, y]);
                        flag = true;
                    }
                }
            }
            virusPos[k] = newPos;
        }
        if (!flag) break;
    }

    return arr[X - 1][Y - 1];
};

console.log(solve())
