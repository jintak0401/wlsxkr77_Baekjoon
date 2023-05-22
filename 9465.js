const fs = require('fs');
const max = (a, b) => a < b ? b : a;

const solve = () => {
    const input = fs.readFileSync("/dev/stdin").toString().split("\n");
    let inputIdx = 0;
    const TC = +input[inputIdx++];

    for (let tc = 0; tc < TC; tc++) {
        const M = +input[inputIdx++];
        const arr = Array.from({ length: 2 }, () => input[inputIdx++].split(' ').map(Number));
        // dp[n행][m열][선택여부] = 그 때의 최대 가치
        const dp = Array.from({ length: 2 }, () => Array.from({ length: M }, () => Array.from({ length: 2 }, () => 0)));
        dp[0][0][1] = arr[0][0];
        dp[1][0][1] = arr[1][0];
        for (let i = 1; i < M; i++) {
            dp[0][i][0] = dp[1][i][0] = max(dp[0][i - 1][1], dp[1][i - 1][1]);
            dp[0][i][1] = max(dp[0][i - 1][0], dp[1][i - 1][1]) + arr[0][i];
            dp[1][i][1] = max(dp[1][i - 1][0], dp[0][i - 1][1]) + arr[1][i];
        }
        console.log(Math.max(dp[0][M-1][0], dp[1][M-1][0], dp[0][M-1][1], dp[1][M-1][1]))
    }
};


solve();
