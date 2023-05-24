const fs = require('fs');

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');
    let inputIdx = 0;
    const N = +input[inputIdx++]
    const M = +input[inputIdx++]
    const betweenUnits = [];
    let prevVip = 0;
    for (let i = 0; i < M; i++) {
        const vip = +input[inputIdx++];
        betweenUnits.push(vip - prevVip - 1)
        prevVip = vip;
    }
    betweenUnits.push(N - prevVip)

    const dp = Array(Math.max(...betweenUnits) + 1).fill(0);
    dp[0] = dp[1] = 1;
    for (let i = 2; i < dp.length; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    let ans = 1;

    for (const unit of betweenUnits) {
        ans *= dp[unit];
    }

    return ans;
};

console.log(solve())
