const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const [N, M] = input[inputIdx++].split(' ').map((v) => +v);
	let arr = input[inputIdx].split(' ').map((v) => +v);
	arr.push(0);
	arr = arr.sort((a, b) => a - b);

	const bisectLeft = (a, x, lo = 0, hi = a.length) => {
		let mid;
		while (lo < hi) {
			mid = Math.floor((lo + hi) / 2);
			x <= a[mid] ? (hi = mid) : (lo = mid + 1);
		}
		return lo;
	};

	const pivot = bisectLeft(arr, 0);

	let ans = 0;
	for (let i = 0; i < pivot; i += M) {
		ans += -arr[i] * 2;
	}
	for (let i = N; i > pivot; i -= M) {
		ans += arr[i] * 2;
	}
	ans -= -arr[0] < arr[N] ? arr[N] : -arr[0];
	return ans;
}

console.log(solve());
