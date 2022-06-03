const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const [N, C] = input[inputIdx++].split(' ').map((v) => +v);
	const arr = input[inputIdx++].split(' ').map((v) => +v);

	const combi = (a, idx, ret) => {
		if (idx === a.length) return;
		let weight;
		const len = ret.length;
		for (let i = 0; i < len; i++) {
			if ((weight = ret[i] + a[idx]) <= C) {
				ret.push(weight);
			}
		}
		combi(a, idx + 1, ret);
	};
	const w1 = [0],
		w2 = [0];
	combi(arr.slice(0, Math.floor(N / 2)), 0, w1);
	combi(arr.slice(Math.floor(N / 2)), 0, w2);
	w1.sort((a, b) => a - b);
	w2.sort((a, b) => a - b);

	let ans = 0;
	for (let i = 0, j = w2.length - 1; i < w1.length && j >= 0; i++) {
		while (w1[i] + w2[j] > C) j--;
		ans += j + 1;
	}

	console.log(ans);
}

solve();
