const fs = require('fs')

function solve() {
    const input = fs.readFileSync("/dev/stdin").toString().split('\n');

    const [_, K] = input.shift().split(' ').map(val => +val);

    const things = input.map(el => el.split(' ').map(v => +v)).filter(([w]) => w <= K).sort((a, b) => a[0] - b[0]);

    const dp = [];
    let ans = 0;
    for (let i = 0; i <= K; dp[i++] = 0);

    things.forEach(([w, v]) => {
        for (let i = K - w; i >= 0; i--) {
            if (i === 0) {
                (dp[w] < v) && (dp[w] = v);
                (ans < dp[w]) && (ans = dp[w]);
            }
            else {
                (dp[i + w] < dp[i] + v) && (dp[i + w] = dp[i] + v);
                (ans < dp[i + w]) && (ans = dp[i + w]);
            }
        }
    });
    console.log(ans);
}

solve();
