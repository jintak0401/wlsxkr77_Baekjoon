const fs = require('fs');

Array.prototype.count = function(num) {
    let ret = 0;
    for (let i = 0; i < this.length; i++) {
        this[i] === num && (ret++);
    }
    return ret;
};

const solve = () => {
    const input = fs.readFileSync("/dev/stdin").toString().split("\n");
    let inputIdx = 0;
    const N = +input[inputIdx++];
    const len = N * N;

    let image = '';
    for (let i = 0; i < N; i++) {
        image += input[inputIdx++];
    }

    const normal = Array(len).fill(-1);
    const weak = Array(len).fill(-1);
    const normalVisited = Array(len).fill(false);
    const weakVisited = Array(len).fill(false);

    function* adj(idx) {
        if (idx - N > 0) yield idx - N;
        if (idx + N < len) yield idx + N;
        if (idx % N) yield idx - 1;
        if ((idx + 1) % N) yield idx + 1;
    }

    const unionFind = (targetSet, idx) => {
        if (targetSet[idx] === -1) return idx;
        return (targetSet[idx] = unionFind(targetSet, targetSet[idx]));
    }

    const dfs = (targetSet, targetVisited, idx, checkCb) => {
        targetVisited[idx] = true;
        for (const newIdx of adj(idx)) {
            if (checkCb(idx, newIdx) && !targetVisited[newIdx]) {
                targetSet[newIdx] = unionFind(targetSet, idx);
                dfs(targetSet, targetVisited, newIdx, checkCb);
            }
        }
    };

    for (let i = 0; i < len; i++) {
        !normalVisited[i] && dfs(normal, normalVisited, i, (idx, newIdx) => image[idx] === image[newIdx]);
        !weakVisited[i] && dfs(weak, weakVisited, i, (idx, newIdx) => {
                if (image[idx] === image[newIdx]) return true;
                else if (image[idx] === 'G' && image[newIdx] === 'R') return true;
                else if (image[idx] === 'R' && image[newIdx] === 'G') return true
                return false;
            },
        );
    }

    console.log(normal.count(-1), weak.count(-1));
};


solve();
