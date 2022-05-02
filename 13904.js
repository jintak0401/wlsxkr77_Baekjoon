const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const N = +input[inputIdx++];

	const work = Array.from({ length: N }, () =>
		input[inputIdx++].split(' ').map((v) => +v)
	);

	work.sort((a, b) => {
		if (a[1] === b[1]) return a[0] - b[0];
		else return b[1] - a[1];
	});

	const done = Array(1000).fill(false);
	let ans = 0;

	for (const [d, w] of work) {
		for (let day = d - 1; day >= 0; day--) {
			if (!done[day]) {
				ans += w;
				done[day] = true;
				break;
			}
		}
	}
	console.log(ans);
}

solve();
