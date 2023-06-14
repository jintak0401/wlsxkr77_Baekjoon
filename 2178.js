const fs = require('fs');
const d = [[0, 1], [1, 0], [0, -1], [-1, 0]];

const genKey = (a, b) => `${a},${b}`;
const parseKey = (key) => key.split(',').map(Number);

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');

    let inputIdx = 0;

    const [N, M] = input[inputIdx++].split(' ').map(Number);

    const maze = Array.from(Array(N), () => input[inputIdx++]);

    const visited = new Set();
    const goalKey = genKey(N - 1, M - 1);
    let ans = 1, que = [`0,0`], nextQ = [], x, y, nextKey;


    while (que.length) {
        nextQ = [];
        while (que.length) {
            const key = que.pop();
            if (visited.has(key)) continue;
            else if (key === goalKey) return ans;
            visited.add(key);

            const [ox, oy] = parseKey(key);
            for (const [dx, dy] of d) {
                x = ox + dx;
                y = oy + dy;
                nextKey = genKey(x, y);
                if (maze[x]?.[y] === '1' && !visited.has(nextKey)) {
                    nextQ.push(nextKey);
                }
            }
        }
        que = nextQ;
        ans++;
    }
};

console.log(solve());
