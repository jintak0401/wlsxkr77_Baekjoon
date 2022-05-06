const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const [N, S] = input[inputIdx++].split(' ').map((v) => +v);

	const arr = input[inputIdx++].split(' ').map((v) => +v);

	const extend = (seq) => {
		let ret = [0];
		for (const s of seq) {
			const tmp = ret.map((v) => v + s);
			ret = ret.concat(tmp);
		}
		return ret;
	};

	const counter = (seq) => {
		const count = {};
		for (const s of seq) {
			count.hasOwnProperty(s) ? (count[s] += 1) : (count[s] = 1);
		}
		return count;
	};

	const idx = Math.floor(N / 2);
	const leftArr = extend(arr.slice(0, idx));
	const rightArr = extend(arr.slice(idx));
	const rightCounter = counter(rightArr);

	let ans = 0;
	for (const v of leftArr) {
		const remain = S - v;
		if (rightCounter.hasOwnProperty(remain)) ans += rightCounter[remain];
	}

	return S === 0 ? ans - 1 : ans;
}

console.log(solve());
