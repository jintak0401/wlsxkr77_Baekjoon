const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const [N, M, H] = input[inputIdx++].split(' ').map((v) => +v);

	let line, installed, tmp;

	(installed = []).length = N;
	installed.fill(0);

	(tmp = []).length = N + 1;
	for (let i = 1; i <= N; i++) tmp[i] = i;

	(line = []).length = H + 1;
	for (let i = 1; i <= H; i++) line[i] = new Set();

	for (let i = 0; i < M; i++) {
		const [a, b] = input[inputIdx++].split(' ').map((v) => +v);
		line[a].add(b);
		installed[b - 1] += 1;
	}

	const checkInstalled = (d) => {
		let val = 0;
		for (const v of installed) {
			if (v % 2) val += 1;
		}
		return val <= 3 - d;
	};

	const check = () => {
		let tmpL = [...tmp];
		for (let i = 1; i <= H; i++) {
			for (const l of line[i]) {
				[tmpL[l], tmpL[l + 1]] = [tmpL[l + 1], tmpL[l]];
			}
		}
		for (let i = 1; i <= N; i++) {
			if (tmpL[i] !== i) return false;
		}
		return true;
	};

	const combi = (maxDepth, curDepth, hor, ver) => {
		if (maxDepth === curDepth) {
			if (check()) return curDepth;
			else return -1;
		} else if (checkInstalled(curDepth)) {
			for (let i = hor; i <= H; i++) {
				for (let j = i === hor ? ver : 1; j < N; j++) {
					if (line[i].has(j - 1) || line[i].has(j) || line[i].has(j + 1))
						continue;
					line[i].add(j);
					installed[j - 1] += 1;
					const ret = combi(maxDepth, curDepth + 1, i, j);
					if (ret !== -1) return ret;
					line[i].delete(j);
					installed[j - 1] -= 1;
				}
			}
		}
		return -1;
	};

	for (let depth = 0; depth <= 3; depth++) {
		const ans = combi(depth, 0, 1, 1);
		if (ans !== -1) return ans;
	}
	return -1;
}

console.log(solve());
