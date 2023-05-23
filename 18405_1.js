const fs = require('fs');

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');
    let inputIdx = 0;
    const [N, K] = input[inputIdx++].split(' ').map(Number);
    const arr = Array.from({length: N}, () => input[inputIdx++].split(' ').map(Number));
    const [S, X, Y] = input[inputIdx++].split(' ').map(Number);
    const dist = Array(K + 1).fill(Infinity);

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (!arr[i][j]) continue;
            const diff = Math.abs(X - 1 - i) + Math.abs(Y - 1 - j);
            if (diff < dist[arr[i][j]]) {
                dist[arr[i][j]] = diff;
            }
        }
    }

    const minDist = Math.min(...dist);
    return minDist <= S ? (dist.findIndex((val) => val === minDist)) : 0;
};

console.log(solve())
