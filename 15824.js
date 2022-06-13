const fs = require('fs');

function solve() {
	// BigInt 사용
	const MOD = 1_000_000_007n;
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const N = +input[inputIdx++];
	const arr = input[inputIdx++]
		.split(' ')
		.map((v) => BigInt(v))
		.sort((a, b) => Number(a - b));

	if (N === 1) return 0;

	const power = [];
	power.length = N;
	power[0] = 1n;
	for (let i = 1; i < N; i++) {
		power[i] = (2n * power[i - 1]) % MOD;
	}

	let tmp,
		ans = 0n;
	for (let i = 0; i < Math.floor(N / 2); i++) {
		tmp = N - 1 - i;
		ans = (ans + (arr[tmp] - arr[i]) * (power[tmp] - power[i])) % MOD;
		// JS 는 -5 % 3 === -2 이므로 음수일 경우 +MOD 해줌
		if (ans < 0) ans += MOD;
	}

	return Number(ans);
}

console.log(solve());
