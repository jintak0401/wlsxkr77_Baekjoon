const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const N = +input[inputIdx++];
	let alpha = {};
	const start = new Set();
	const power = [1];
	for (let i = 0; i < 11; i++) {
		power.push(power[i] * 10);
	}
	for (let i = 0; i < N; i++) {
		const tmp = input[inputIdx++];
		start.add(tmp[0]);
		for (let j = 0; j < tmp.length; j++) {
			alpha[tmp[j]] = (alpha[tmp[j]] || 0) + power[tmp.length - j - 1];
		}
	}

	alpha = Object.entries(alpha).sort((a, b) => b[1] - a[1]);
	if (alpha.length === 10 && start.has(alpha[9][0])) {
		let idx = 8;
		while (start.has(alpha[idx][0])) idx--;
		alpha.push(...alpha.splice(idx, 1));
	}
	let ans = 0;
	let num = 9;
	for (const [_, digit] of alpha) {
		ans += num * digit;
		num--;
	}
	return ans;
}

console.log(solve());
