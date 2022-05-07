const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const [V, E] = input[inputIdx++].split(' ').map((v) => +v);
	let weight, disjointSet;
	(disjointSet = []).length = V + 1;
	for (let i = 1; i <= V; i++) {
		disjointSet[i] = -i;
	}

	(weight = []).length = E;
	for (let i = 0; i < E; i++) {
		weight[i] = input[inputIdx++].split(' ').map((v) => +v);
	}

	weight.sort((a, b) => a[2] - b[2]);

	const find = (x) => {
		if (disjointSet[x] < 0) return x;
		else return (disjointSet[x] = find(disjointSet[x]));
	};

	let count = V - 1,
		idx = 0,
		ans = 0;

	while (count) {
		const [a, b, c] = weight[idx++];
		const [x, y] = [find(a), find(b)];
		if (x !== y) {
			count--;
			ans += c;
			disjointSet[y] = x;
		}
	}

	return ans;
}

console.log(solve());
