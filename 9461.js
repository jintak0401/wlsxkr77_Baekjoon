const fs = require('fs');
const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');

    let inputIdx = 0;
    const TC = +input[inputIdx++];
    const dp = Array(101).fill(0);
    dp[1] = dp[2] = dp[3] = 1;
    dp[4] = dp[5] = 2;
    dp[6] = 3;
    dp[7] = 4;
    dp[8] = 5;
    for (let i = 9; i < dp.length; i++) {
        dp[i] = dp[i-1] + dp[i-5];
    }
    for (let i = 0; i < TC; i++) {
        console.log(dp[+input[inputIdx++]]);
    }
};

solve()
