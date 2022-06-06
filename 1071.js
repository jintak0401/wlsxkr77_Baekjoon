const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const N = +input[inputIdx++];
	const arr = input[inputIdx++]
		.split(' ')
		.map((v) => +v)
		.sort((a, b) => a - b);

	let idx = 0;

	while (idx < N) {
		if (arr[idx] === arr[idx - 1] + 1) {
			let start = idx - 1,
				end = idx + 1;
			for (; start >= 1 && arr[start - 1] === arr[idx - 1]; start--);
			for (; end < N && arr[end] === arr[idx]; end++);
			if (end === N) {
				const before = arr[idx - 1],
					after = arr[idx];
				const midIdx = start + (end - idx);
				for (let i = start; i < midIdx; arr[i++] = after);
				for (let i = midIdx; i < end; arr[i++] = before);
			} else {
				[arr[idx], arr[end]] = [arr[end], arr[idx]];
			}
			idx = end + 1;
		} else {
			idx++;
		}
	}
	console.log(...arr);
}

solve();
