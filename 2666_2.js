const fs = require('fs');
const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');
    let inputIdx = 0;
    const N = +input[inputIdx++];
    const [l, r] = input[inputIdx++].split(' ').map(Number);
    const len = +input[inputIdx++];
    const arr = Array.from({length: len}, () => +input[inputIdx++]);
    let ans = Infinity;

    const dfs = (depth, l, r, cost) => {
        if (cost > ans) return;
        else if (depth === len) {
            if (cost < ans) ans = cost;
            return;
        }

        const pos = arr[depth];
        if (pos <= l) {
            dfs(depth + 1, pos, r, cost + l - pos);
        }
        else if (r <= pos) {
            dfs(depth + 1, l, pos, cost + pos - r);
        }
        else {
            dfs(depth + 1, pos, r, cost + pos - l);
            dfs(depth + 1, l, pos, cost + r - pos);
        }
    }
    dfs(0, l, r, 0);

    return ans;

};

console.log(solve())
