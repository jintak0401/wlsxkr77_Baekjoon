const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf-8').toString().trim().split('\n');

const solve = (N, K) => {
    const visited = new Set([]);
    let que = [N], nextQue = [], ans = 0;

    while (que.length) {
        while (que.length) {
            const pos = que.pop();
            if (visited.has(pos)) continue;
            visited.add(pos);
            if (pos === K) return ans;
            if (pos - 1 >= 0) nextQue.push(pos - 1);
            if (pos + 1 <= 100000) nextQue.push(pos + 1);
            if (pos * 2 <= 100000) nextQue.push(pos * 2);
        }
        que = nextQue;
        nextQue = [];
        ans++;
    }
};

console.log(solve(...input[0].split(' ').map(Number)));
