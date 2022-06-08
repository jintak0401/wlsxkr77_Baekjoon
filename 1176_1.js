const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const [N, K] = input[inputIdx++].split(' ').map((v) => +v);
	const arr = [];
	arr.length = N;
	for (let i = 0; i < N; arr[i++] = +input[inputIdx++]);

	const dp = [];
	const totalBit = 1 << N;
	dp.length = N;
	for (let i = 0; i < N; i++) {
		dp[i] = [];
		dp[i].length = totalBit;
		for (let j = 0; j < totalBit; dp[i][j++] = 0);
		dp[i][1 << i] = 1;
	}

	let tmp;
	for (let visited = 1; visited < totalBit; visited++) {
		// i: 앞에 서는 학생
		for (let i = 0; i < N; i++) {
			// j: 뒤에 서는 학생
			for (let j = 0; j < N; j++) {
				if ((visited & (tmp = 1 << j)) === 0 && Math.abs(arr[i] - arr[j]) > K) {
					dp[j][visited | tmp] += dp[i][visited];
				}
			}
		}
	}

	let ans = 0;
	for (let i = 0; i < N; i++) {
		ans += dp[i].at(-1);
	}

	console.log(ans);
}

solve();
