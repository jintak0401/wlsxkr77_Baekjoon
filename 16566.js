const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const [N, M, K] = input[inputIdx++].split(' ').map((v) => +v);

	const cards = input[inputIdx++]
		.split(' ')
		.map((v) => +v)
		.sort((a, b) => a - b);

	const enemyCards = input[inputIdx++].split(' ').map((v) => +v);

	const disjointSet = [];
	disjointSet.length = M + 1;
	for (let i = 0; i < M + 1; disjointSet[i++] = -1);

	const union_find = (a) => {
		if (disjointSet[a] === -1) return a;
		disjointSet[a] = union_find(disjointSet[a]);
		return disjointSet[a];
	};

	const bisect = (x) => {
		let lo = 0,
			hi = M,
			mid;
		while (lo < hi) {
			mid = Math.floor((lo + hi) / 2);
			if (x < cards[union_find(mid)]) hi = mid;
			else lo = mid + 1;
		}
		return union_find(lo);
	};

	let ans = '';
	for (const enemy of enemyCards) {
		const idx = bisect(enemy);
		disjointSet[idx] = union_find(idx + 1);
		ans += `${cards[idx]}\n`;
	}

	console.log(ans);
}

solve();
