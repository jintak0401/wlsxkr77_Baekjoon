const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const N = +input[inputIdx++];
	const outDegree = [];
	const time = [];
	const ans = [];
	outDegree.length = N + 1;
	time.length = N + 1;
	ans.length = N + 1;
	for (let i = 1; i <= N; ans[i++] = -1);

	for (let i = 1; i <= N; i++) {
		const [t, ...need] = input[inputIdx++].split(' ').map((v) => +v);
		time[i] = t;
		outDegree[i] = need.slice(0, -1);
		if (outDegree[i].length === 0) ans[i] = t;
	}

	const dfs = (node) => {
		if (ans[node] !== -1) return ans[node];
		let max = -1;
		for (const nxt of outDegree[node]) {
			const tmp = dfs(nxt);
			max < tmp && (max = tmp);
		}
		return (ans[node] = max + time[node]);
	};

	for (let i = 1; i <= N; i++) {
		console.log(dfs(i));
	}
}

solve();
