const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const [N, M] = input[inputIdx++].split(' ').map((v) => +v);
	const arr = input[inputIdx++].split(' ').map((v) => +v);

	const possible = (val) => {
		let cnt = 1,
			sum = 0;
		for (const num of arr) {
			if (sum + num <= val) {
				sum += num;
			} else {
				cnt++;
				sum = num;
			}
		}
		return cnt <= M;
	};

	const divide = (val) => {
		let cnt = 0,
			sum = 0,
			m = M,
			ret = [];
		for (let i = 0; i < N; i++) {
			if (sum + arr[i] <= val) {
				cnt++;
				sum += arr[i];
			} else {
				m--;
				sum = arr[i];
				ret.push(cnt);
				cnt = 1;
			}
			if (N - i === m) break;
		}

		while (m) {
			ret.push(cnt);
			cnt = 1;
			m--;
		}

		return ret;
	};

	let lo = Math.max(...arr),
		hi = arr.reduce((prev, cur) => prev + cur, 0);

	while (lo <= hi) {
		const mid = Math.floor((lo + hi) / 2);
		possible(mid) ? (hi = mid - 1) : (lo = mid + 1);
	}

	console.log(lo);
	console.log(...divide(lo));
}

solve();
