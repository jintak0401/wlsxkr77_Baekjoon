const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const N = +input[inputIdx++];
	const arr = input[inputIdx++].split(' ').map((v) => +v);
	const ans = [];
	ans.length = N;
	const stack = [];

	for (let i = 0; i < N; i++) {
		while (stack.length && arr[stack[stack.length - 1]] < arr[i]) {
			ans[stack.pop()] = arr[i];
		}
		stack.push(i);
	}
	for (const i of stack) ans[i] = -1;
	console.log(ans.join(' '));
}

solve();
