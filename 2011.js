const fs = require('fs');

const MOD = 1_000_000;

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n')[0];
    if (input[0] === '0') return 0;

    const len = input.length;
    const dp = Array(len).fill(0);
    dp[0] = 1;

    for (let i = 1; i < len; i++) {
        if (input[i] > '0') dp[i] = dp[i-1];
        const num = Number(input[i - 1] + input[i]);
        if (10 <= num && num <= 26) {
            dp[i] = (dp[i] + (dp[i-2] ?? 1)) % MOD;
        }
    }
    return dp[len - 1];
};

console.log(solve());
