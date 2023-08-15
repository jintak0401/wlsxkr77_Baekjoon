const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf-8').toString().trim().split('\n');

const PREFIX = '--';

const solve = (N, ...arr) => {
    const ans = {};

    for (const line of arr) {
        const [unit, ...rooms] = line.split(' ');
        let obj = ans;
        for (const room of rooms) {
            if (!obj[room]) {
                obj[room] = {};
            }
            obj = obj[room];
        }
    }

    const dfs = (depth, obj) => {
        for (const room of Object.keys(obj).sort()) {
            console.log(PREFIX.repeat(depth) + room);
            dfs(depth + 1, obj[room]);
        }
    }

    dfs(0, ans);
};

solve(Number(input[0]), ...input.slice(1))
