const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf-8').toString().trim().split('\n');

const solve = (N, arr) => {
    let ans = [N];

    for (let i = N - 2; i >= 0; i--) {
        ans = [...ans.slice(0, arr[i]), i + 1, ...ans.slice(arr[i])];
    }

    return ans;
};

console.log(...solve(Number(input[0]), input[1].split(' ').map(Number)));
