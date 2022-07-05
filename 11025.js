const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	let [N, K] = input[inputIdx++].split(' ').map(v => +v);

	let ans = 0;

	for (let i = 2; i <= N; i++){
		ans = (ans + K) % i;
	}

	return ans + 1;
}

console.log(solve());
