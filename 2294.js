const fs = require('fs');

const min = (a, b) => (a < b ? a : b);

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');

    let inputIdx = 0;
    const [N, K] = input[inputIdx++].split(' ').map(Number);
    const coins = [...new Set(Array.from(Array(N), () => Number(input[inputIdx++])))].sort((a, b) => a - b);

    const dp = Array(K + 1).fill(Infinity);
    dp[0] = 0;

    for (let i = 0; i < coins.length; i++){
        const coin = coins[i];
        for (let j = coin; j <= K; j++) {
            dp[j] = min(dp[j], dp[j-coin] + 1);
        }
    }

    return dp[K] === Infinity ? -1 : dp[K];
};

console.log(solve());
