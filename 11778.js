const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	// BigInt 이용
	const mod = 1_000_000_007n;

	const GCD = (x, y) => {
		while (y) {
			[x, y] = [y, x % y];
		}
		return x;
	};

	const mulMat = (mat1, mat2) => {
		const ret = [
			[0n, 0n],
			[0n, 0n],
		];
		for (let i = 0; i < 2; i++) {
			for (let j = 0; j < 2; j++) {
				for (let k = 0; k < 2; k++) {
					ret[i][j] += mat1[i][k] * mat2[k][j];
				}
				ret[i][j] %= mod;
			}
		}
		return ret;
	};

	const fibonacci = (num) => {
		if (num <= 2) return 1;

		let ans = [
			[1n, 0n],
			[0n, 1n],
		];
		let mat = [
			[1n, 1n],
			[1n, 0n],
		];
		while (num) {
			if (num % 2n) ans = mulMat(ans, mat);
			mat = mulMat(mat, mat);
			num /= 2n;
		}
		return ans[0][1];
	};

	const [N, M] = input[inputIdx++].split(' ').map((v) => BigInt(v));

	return Number(fibonacci(GCD(N, M)));
}

console.log(solve());
