const fs = require('fs');

const getMax = (a, b) => a < b ? b : a;
const getMin = (a, b) => a < b ? a : b;
const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');

    let inputIdx = 0;

    const [N, M] = input[inputIdx++].split(' ').map(Number);
    const arr = Array.from(Array(N), () => +input[inputIdx++]);

    if (N === 1) return arr[0];

    const contain = Array.from(Array(N + 1), () => Array(M + 1).fill(-Infinity));
    const notContain = Array.from(Array(N + 1), () => Array(M + 1).fill(-Infinity));
    for (let i = 0; i <= N; i++) {
        notContain[i][0] = contain[i][0] = 0;
    }

    for (let i = 1; i <= N; i++) {
        for (let j = 1; j <= getMin(M, Math.floor((i + 1) / 2)); j++) {
            contain[i][j] = getMax(contain[i-1][j], notContain[i-1][j-1]) + arr[i-1];
            notContain[i][j] = getMax(contain[i-1][j], notContain[i-1][j]);
        }
    }

    return getMax(contain[N][M], notContain[N][M]);
};

console.log(solve());
