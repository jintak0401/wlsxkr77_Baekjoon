const fs = require('fs')

function solve() {
    let input = fs.readFileSync("/dev/stdin").toString().split("\n");

    if (input[0] === '100') return 0;

    const channel = parseInt(input[0]);
    const possibleNums = Array.from({length: 10}, () => true);
    (input[2].split(' ') || []).forEach((num) => (possibleNums[parseInt(num)] = false));

    let ans = Math.abs(channel - 100);
    let val;

    for (let i = 0; i < 1000000; i++){
        const cur = i.toString();
        let j = 0;
        for (; j < cur.length; j++){
            if (!possibleNums[cur[j]]) break;
        }
        if (j === cur.length && (val = Math.abs(channel - cur) + cur.length) < ans) {
            ans = val;
        }
    }
    return ans;
}

console.log(solve());
