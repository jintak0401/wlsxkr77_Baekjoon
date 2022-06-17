const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const N = +input[inputIdx++];
	const arr = input[inputIdx++].split(' ').map((v) => +v);
	const len = [];
	len.length = N + 1;
	for (let i = 0; i < N + 1; len[i++] = 0);

	for (const num of arr) {
		len[num] = len[num - 1] + 1;
	}

	return N - Math.max(...len);
}

console.log(solve());
