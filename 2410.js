const fs = require('fs');

const MOD = 1_000_000_000;

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');

    const N = +input[0];

    const dp = Array.from(Array(N + 1).fill(0));
    dp[1] = 1;

    for (let i = 2; i <= N; i++) {
        if (i % 2) {
            dp[i] = dp[i-1];
        }
        else {
            dp[i] = (dp[i-1] + dp[i/2]) % MOD;
        }
    }

    return dp[N];

};

console.log(solve());
