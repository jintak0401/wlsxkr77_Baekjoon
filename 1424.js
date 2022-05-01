const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const N = +input[inputIdx++];
	const L = +input[inputIdx++];
	const C = +input[inputIdx++];

	let numSongInOne = Math.min(Math.floor((C + 1) / (L + 1)), N);

	if (numSongInOne % 13 === 0) numSongInOne--;

	let numCd = Math.floor(N / numSongInOne);

	const remain = N % numSongInOne;

	if (remain > 0) {
		if (remain % 13 === 0 && remain + 1 === numSongInOne) numCd += 2;
		else numCd += 1;
	}

	console.log(numCd);
}

solve();
