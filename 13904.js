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

	const maxDate = Math.max(...Array.from({ length: N }, (v, i) => work[i][0]));
	const doing = Array(maxDate).fill(0);
	let day = 0,
		ans = 0;

	for (const [d, w] of work) {
		for (day = d - 1; day >= 0 && doing[day] !== 0; day--);
		if (day >= 0) {
			doing[day] = w;
			ans += w;
		}
	}

	console.log(ans);
}

solve();
