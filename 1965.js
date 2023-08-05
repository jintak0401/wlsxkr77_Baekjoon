const fs = require('fs');

const bisectLeft = (a, x) => {
    let lo = 0,
        hi = a.length;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        x <= a[mid] ? (hi = mid) : (lo = mid + 1);
    }
    return lo;
};

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');

    let inputIdx = 0;
    const N = +input[inputIdx++];
    const arr = input[inputIdx++].split(' ').map(Number);

    const dp = [];

    arr.forEach((x) => {
        dp[bisectLeft(dp, x)] = x;
    })

    return dp.length;
};

console.log(solve());
