const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const N = +input[inputIdx++];
	const arr = input[inputIdx++].split(' ').map((v) => +v);

	const bisectLeft = (a, x) => {
		let lo = 0,
			hi = a.length;
		while (lo < hi) {
			const mid = Math.floor((lo + hi) / 2);
			x <= a[mid] ? (hi = mid) : (lo = mid + 1);
		}
		return lo;
	};

	const dp = [arr[0]];

	for (let i = 1; i < N; i++) {
		const num = arr[i];
		if (dp.at(-1) < num) dp.push(num);
		else dp[bisectLeft(dp, num)] = num;
	}

	console.log(dp.length);
}

solve();
