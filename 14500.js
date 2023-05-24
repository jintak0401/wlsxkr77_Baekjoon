const fs = require('fs');

const dr = [[0, -1], [-1, 0], [-1, 1], [0, 2], [1, 1], [1, 0]];
const dd = [[0, -1], [-1, 0], [0, 1], [1, 1], [2, 0], [1, -1]];

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');
    let inputIdx = 0;
    const [N, M] = input[inputIdx++].split(' ').map(Number);
    const arr = Array.from({length: N}, () => input[inputIdx++].split(' ').map(Number));

    const getSumMaxes = (ox, oy, isRight) => {
        const d = isRight ? dr : dd;
        let first = -1, second = -1;

        for (const [dx, dy] of d) {
            const x = ox + dx, y = oy + dy;
            if (!arr[x]?.[y]) continue;
            else if (first < arr[x][y]) {
                second = first;
                first = arr[x][y];
            }
            else if (second < arr[x][y]) second = arr[x][y];
        }
        return first + second;
    }


    let ans = 0, val;
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (arr[i]?.[j+1]) {
                val = arr[i][j] + arr[i][j+1] + getSumMaxes(i, j, true);
                ans < val && (ans = val);
            }
            if (arr[i+1]?.[j]) {
                val = arr[i][j] + arr[i+1][j] + getSumMaxes(i, j, false);
                ans < val && (ans = val);
            }
        }
    }

    return ans;
};

console.log(solve())
