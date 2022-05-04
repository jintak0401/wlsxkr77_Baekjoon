const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const N = +input[inputIdx++];

	let tree, visited;

	(tree = []).length = N + 1;
	for (let i = 1; i <= N; i++) tree[i] = [];

	for (let i = 0; i < N - 1; i++) {
		const [a, b] = input[inputIdx++].split(' ').map((v) => +v);
		tree[a].push(b);
		tree[b].push(a);
	}

	(visited = []).length = N + 1;
	visited.fill(false);

	// ans1: 선택됨, ans2: 선택안됨
	const dfs = (idx) => {
		let ans1 = 1,
			ans2 = 0;
		visited[idx] = true;

		for (const nxt of tree[idx]) {
			if (!visited[nxt]) {
				const [tmp1, tmp2] = dfs(nxt);
				ans1 += tmp1 < tmp2 ? tmp1 : tmp2;
				ans2 += tmp1;
			}
		}
		return [ans1, ans2];
	};

	const [ans1, ans2] = dfs(1);
	return ans1 < ans2 ? ans1 : ans2;
}

console.log(solve());
