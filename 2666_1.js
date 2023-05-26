const fs = require('fs');
const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');
    let inputIdx = 0;

    const N = +input[inputIdx++];
    const [l, r] = input[inputIdx++].split(' ').map(Number);
    const len = +input[inputIdx++];
    const arr = Array.from({length: len}, () => +input[inputIdx++]);
    // dp[left][right] = [round, cost];
    let dp = {}, nextDp;
    let stack = [[l, r]], nextStack;

    const genKey = (a, b) => `${a},${b}`;
    const parseKey = (str) => str.split(',');

    dp[genKey(l, r)] = 0;
    for (let i = 1; i <= len; i++) {
        nextStack = [];
        nextDp = {};
        const pos = arr[i-1];
        while (stack.length) {
            const [l, r] = stack.pop();
            const beforeCost = dp[genKey(l, r)];
            // 왼쪽 문 움직임
            if (pos <= l) {
                const nextKey = genKey(pos, r);
                const curCost = beforeCost + l - pos;
                (!nextDp[nextKey] || curCost < nextDp[nextKey]) && (nextDp[nextKey] = curCost, nextStack.push([pos, r]));
            }
            // 오른쪽 문 움직임
            else if (pos >= r) {
                const nextKey = genKey(l, pos);
                const curCost = beforeCost + pos - r;
                (!nextDp[nextKey] || curCost < nextDp[nextKey]) && (nextDp[nextKey] = curCost, nextStack.push([l, pos]));
            }
            // 양쪽 모두 움직임
            else {
                const nextLKey = genKey(pos, r);
                const nextRKey = genKey(l, pos);
                const curLCost = beforeCost + pos - l;
                const curRCost = beforeCost + r - pos;
                (!nextDp[nextLKey] || curLCost < nextDp[nextLKey]) && (nextDp[nextLKey] = curLCost, nextStack.push([pos, r]));
                (!nextDp[nextRKey] || curRCost < nextDp[nextRKey]) && (nextDp[nextRKey] = curRCost, nextStack.push([l, pos]));
            }
        }
        stack = nextStack;
        dp = nextDp;
    }

    return Math.min(...stack.map(([l, r]) => dp[genKey(l, r)]));
};

console.log(solve())
