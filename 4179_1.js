const fs = require('fs');

const d = [[0, 1], [1, 0], [0, -1], [-1, 0]];

const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');
    let inputIdx = 0;
    const [R, C] = input[inputIdx++].split(' ').map(Number);

    const board = Array.from(Array(R), () => input[inputIdx++].split(''));

    const visited = Array.from(Array(R), () => Array(C).fill(false));
    let personPos = [], nextPersonPos = [];
    let firePos = [];

    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (board[i][j] === 'F') {
                firePos.push([i, j]);
            }
            else if (board[i][j] === 'J') {
                board[i][j] = '.';
                personPos.push([i, j]);
            }
        }
    }

    const fireDiffusion = () => {
        const newFirePos = [];
        for (const [or, oc] of firePos) {
            for (const [dr, dc] of d) {
                const r = or + dr;
                const c = oc + dc;
                if (board[r]?.[c] === '.') {
                    board[r][c] = 'F';
                    newFirePos.push([r, c]);
                }
            }
        }
        firePos = newFirePos;
    }

    let ans = 1;
    while (personPos.length) {
        while (personPos.length) {
            const [or, oc] = personPos.pop();
            if (visited[or][oc] || board[or][oc] === 'F') continue;

            visited[or][oc] = true;
            for (const [dr, dc] of d) {
                const r = or + dr;
                const c = oc + dc;
                if (board[r]?.[c] === undefined) {
                    return ans;
                }
                else if (board[r][c] === '.' && !visited[r][c]) {
                    nextPersonPos.push([r, c]);
                }
            }
        }
        fireDiffusion();
        personPos = nextPersonPos;
        nextPersonPos = [];
        ans++;
    }

    return 'IMPOSSIBLE';
};

console.log(solve());
