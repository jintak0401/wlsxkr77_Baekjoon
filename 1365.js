const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const N = +input[inputIdx++];
	const arr = input[inputIdx++].split(' ').map((v) => +v);
	const dp = [arr[0]];

	const bisect = (x) => {
		let lo = 0,
			hi = dp.length;
		while (lo < hi) {
			const mid = Math.floor((lo + hi) / 2);
			x <= dp[mid] ? (hi = mid) : (lo = mid + 1);
		}
		return lo;
	};

	for (let i = 1; i < N; i++) {
		if (dp.at(-1) < arr[i]) dp.push(arr[i]);
		else dp[bisect(arr[i])] = arr[i];
	}

	console.log(N - dp.length);
}

solve();
