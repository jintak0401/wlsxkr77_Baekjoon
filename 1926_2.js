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

    const bfs = (r, c) => {
        let que = [[r, c]], nextQue = [];
        let ret = 0;

        while (que.length) {
            while (que.length) {
                const [ox, oy] = que.pop();
                if (visited[ox][oy]) continue;

                visited[ox][oy] = true;
                ret++;

                for (const [dx, dy] of d) {
                    const x = ox + dx;
                    const y = oy + dy;

                    if (arr[x]?.[y] && !visited[x][y]) {
                        nextQue.push([x, y]);
                    }
                }
            }
            que = nextQue;
            nextQue = [];
        }

        return ret;
    }

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (arr[i][j] && !visited[i][j]) {
                ans[0]++;
                ans[1] = max(ans[1], bfs(i, j));
            }
        }
    }

    console.log(ans[0]);
    console.log(ans[1]);

};

solve()
