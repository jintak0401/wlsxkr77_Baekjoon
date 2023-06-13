const fs = require('fs');
const solve = () => {
    const input = fs.readFileSync('/dev/stdin').toString().split('\n');

    let inputIdx = 0;
    const N = +input[inputIdx++];

    const arr = Array.from(Array(N), () => input[inputIdx++].split(' ').map(Number)).sort((a, b) => a[0] - b[0]);

    const maxColumns = arr.reduce((acc, cur) => {
        if (acc[0][1] < cur[1]) {
            acc = [cur];
        }
        else  if (acc[0][1] === cur[1]) {
            acc.push(cur);
        }
        return acc;
    }, [[-1, -1]]);
    const maxHeight = maxColumns[0][1];

    const getArea = (dir = 1) => {
        let area = 0;
        let idx = dir === 1 ? 0 : N - 1;

        if (arr[idx][1] === maxHeight) return 0;

        let before = arr[idx];
        for (idx += dir; arr[idx][1] !== maxHeight; idx += dir) {
            // 이전보다 높이가 높은 경우
            if (before[1] < arr[idx][1]) {
                area += before[1] * Math.abs(before[0] - arr[idx][0]);
                before = arr[idx];
            }
        }
        area += before[1] * Math.abs(before[0] - arr[idx][0]);
        return area;
    }

    return getArea(1) + getArea(-1) + maxColumns[0][1] * (maxColumns.at(-1)[0] - maxColumns[0][0] + 1);
};

console.log(solve());
