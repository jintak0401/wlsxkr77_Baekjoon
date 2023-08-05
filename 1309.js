const fs = require('fs');

const MOD = 9901;

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');

    const N = +input[0];

    const dp = Array(N + 1).fill(0);
    dp[0] = 1;
    dp[1] = 3;

    for (let i = 2; i <= N; i++) {
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % MOD;
    }

    return dp[N];
};

console.log(solve());
