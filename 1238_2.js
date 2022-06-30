const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const inf = 1_000_000_000;

	const [N, M, X] = input[inputIdx++].split(' ').map((v) => +v);

	// arr 초기화
	const arr = [];
	arr.length = N + 1;
	for (let i = 1; i <= N; i++) {
		arr[i] = [];
		arr[i].length = N + 1;
		for (let j = 1; j <= N; j++) {
			arr[i][j] = inf;
		}
		arr[i][i] = 0;
	}

	for (let i = 0; i < M; i++) {
		const [from, to, dist] = input[inputIdx++].split(' ').map((v) => +v);
		arr[from][to] = dist;
	}

	let tmp;
	for (let k = 1; k <= N; k++) {
		for (let i = 1; i <= N; i++) {
			for (let j = 1; j <= N; j++) {
				if ((tmp = arr[i][k] + arr[k][j]) < arr[i][j]) arr[i][j] = tmp;
			}
		}
	}

	let max = -1;
	for (let i = 1; i <= N; i++) {
		if (max < (tmp = arr[i][X] + arr[X][i])) max = tmp;
	}

	return max;
}

console.log(solve());
