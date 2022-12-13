const fs = require('fs');

function solve() {
    let input = fs.readFileSync('/dev/stdin').toString().split('\n');
    let inputIdx = 0;

    const N = +input[inputIdx++];
    const map = [];
    map.length = N;
    for (let i = 0; i < N; i++) {
        map[i] = input[inputIdx++].split(' ').map(v => +v);
    }

    // 0: 가로, 1: 대각, 2: 세로
    const dp = [];
    dp.length = 3;
    for (let i = 0; i < 3; i++) {
        dp[i] = [];
        dp[i].length = 2;
        for (let j = 0; j < 2; j++) {
            dp[i][j] = [];
            dp[i][j].length = N;
            for (let k = 0; k < N; dp[i][j][k++] = 0) ;
        }
    }
    dp[0][0][1] = 1;

    let jdx;
    for (let j = 0; j < N; j++) {
        for (let k = 2; k < N; k++) {
            for (let i = 0; i < 3; i++) {
                switch (i) {
                    case 0:
                        if (map[j][k]) {
                            dp[0][j % 2][k] = 0;
                            continue;
                        }
                        jdx = j % 2;
                        dp[0][jdx][k] = dp[0][jdx][k - 1] + dp[1][jdx][k - 1];
                        break;
                    case 1:
                        if (map[j][k] || map[j][k - 1] || (0 < j && map[j - 1][k])) {
                            dp[1][j % 2][k] = 0;
                            continue;
                        }
                        jdx = (j + 1) % 2;
                        dp[1][j % 2][k] = j >= 1 ? (dp[0][jdx][k - 1] + dp[1][jdx][k - 1] + dp[2][jdx][k - 1]) : 0;
                        break;
                    case 2:
                        if (map[j][k]) {
                            dp[2][j % 2][k] = 0;
                            continue;
                        }
                        jdx = (j + 1) % 2;
                        dp[2][j % 2][k] = j >= 1 ? (dp[1][jdx][k] + dp[2][jdx][k]) : 0;
                        break;
                }
            }
        }

        jdx = (j + 1) % 2;
        for (let k = 0; k < N; k++){
            dp[0][jdx][k] = 0;
            dp[1][jdx][k] = 0;
            dp[2][jdx][k] = 0;
        }
    }
    jdx = (N - 1) % 2;
    console.log(dp[0][jdx][N - 1] + dp[1][jdx][N - 1] + dp[2][jdx][N - 1]);
}

solve();
