const fs = require('fs');


const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');

    let inputIdx = 0;

    const N = +input[inputIdx++];

    const arr = Array.from(Array(N), () => +input[inputIdx++]).sort((a, b) => a - b);

    let ans = 0;
    for (let i = 0; i < N; i++) {
        ans += Math.abs(arr[i] - i - 1);
    }

    return ans;
};

console.log(solve());
