const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const N = +input[inputIdx++];
	const K = +input[inputIdx++];

	let lo = 1,
		hi = K;
	while (lo <= hi) {
		const mid = Math.floor((lo + hi) / 2);

		let count = 0;
		for (let i = 1; i <= N; i++) {
			const val = Math.floor(mid / i);
			count += val < N ? val : N;
		}
		if (K <= count) hi = mid - 1;
		else lo = mid + 1;
	}
	console.log(lo);
}

solve();
