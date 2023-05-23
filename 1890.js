const fs = require('fs');

const solve = () => {
    const input = fs.readFileSync("/dev/stdin").toString().split("\n");
    let inputIdx = 0;
    const N = +input[inputIdx++];
    const arr = Array.from({length: N}, () => input[inputIdx++].split(' ').map(Number));
    const dp = Array.from({length: N}, () => Array(N).fill(-1n));

    const dfs = (r, c) => {
        // 도착 지점
        if (r === N - 1 && c === N - 1) return 1n;
        // 범위 바깥 or 더 이상 움직일 수 없는 곳
        else if (!arr[r]?.[c]) return 0n;
        // 이미 지나온 곳
        else if (dp[r][c] !== -1n) return dp[r][c];
        return dp[r][c] = dfs(r + arr[r][c], c) + dfs(r, c + arr[r][c]);
    }

    console.log(dfs(0, 0).toString());
};


solve();
