const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	const str = input[0];
	const N = str.length;
	const ans = [];
	ans.length = N + 1;
	for (let i = 0; i <= N; ans[i++] = 2500);
	ans[0] = 1;
	ans[N] = 0;

	for (let i = 0; i < 2 * N - 1; i++) {
		let start = Math.floor(i / 2),
			end = Math.floor((i + 1) / 2);
		while (0 <= start && end < N) {
			if (str[start] === str[end]) {
				const val = ans[start > 0 ? start - 1 : N] + 1;
				if (val < ans[end]) {
					ans[end] = val;
				}
				start--;
				end++;
			} else break;
		}
	}

	console.log(ans[N - 1]);
}

solve();
