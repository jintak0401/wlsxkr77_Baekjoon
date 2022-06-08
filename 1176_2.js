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
		/* 0이 아니라 -1로 초기화하는 이유는
		 * 해당 케이스일 때 가능한 경우의 수가 0인 것과
		 * 구분을 해주기 위함 */
		for (let j = 0; j < totalBit; dp[i][j++] = -1);
	}

	const dfs = (idx, visited) => {
		if (dp[idx][visited] > -1) return dp[idx][visited];
		else if (visited === totalBit - 1) return 1;

		let ret = 0;
		for (let nxt = 0; nxt < N; nxt++) {
			const bit = 1 << nxt;
			if ((bit & visited) === 0 && Math.abs(arr[idx] - arr[nxt]) > K) {
				ret += dfs(nxt, visited | bit);
			}
		}
		dp[idx][visited] = ret;
		return ret;
	};

	let ans = 0;
	for (let i = 0; i < N; i++) {
		ans += dfs(i, 1 << i);
	}

	console.log(ans);
}

solve();
