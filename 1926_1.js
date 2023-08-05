const fs = require('fs');

const max = (a, b) => (a > b ? a : b);

const d = [[0, 1], [1, 0], [0, -1], [-1, 0]];

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');

    let inputIdx = 0;
    const [N, M] = input[inputIdx++].split(' ').map(Number);

    const arr = Array.from(Array(N), () => input[inputIdx++].split(' ').map(Number));

    const visited = Array.from(Array(N), () => Array(M).fill(false));

    const ans = [0, 0];

    const dfs = (ox, oy) => {
        let ret = 1;
        visited[ox][oy] = true;
        for (const [dx, dy] of d) {
            const x = ox + dx;
            const y = oy + dy;
            if (arr[x]?.[y] && !visited[x][y]) {
                ret += dfs(x, y)
            }
        }
        return ret;
    }

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (arr[i][j] && !visited[i][j]) {
                ans[0]++;
                ans[1] = max(ans[1], dfs(i, j));
            }
        }
    }

    console.log(ans[0]);
    console.log(ans[1]);

};

solve()
