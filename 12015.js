const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const N = +input[inputIdx++];
	const arr = input[inputIdx++].split(' ').map((v) => +v);

	let dp = [arr[0]];

	const bisectLeft = (x) => {
		let mid,
			lo = 0,
			hi = dp.length;
		while (lo < hi) {
			mid = Math.floor((lo + hi) / 2);
			dp[mid] < x ? (lo = mid + 1) : (hi = mid);
		}
		return lo;
	};

	for (let i = 1; i < N; i++) {
		if (dp[dp.length - 1] < arr[i]) dp.push(arr[i]);
		else dp[bisectLeft(arr[i])] = arr[i];
	}
	return dp.length;
}

console.log(solve());
