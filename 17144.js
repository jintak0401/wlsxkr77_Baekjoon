const fs = require('fs');

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const [R, C, T] = input[inputIdx++].split(' ').map((v) => +v);
	const len = R * C;
	let arr = [];
	for (let i = 0; i < R; i++) {
		arr.push(...input[inputIdx++].split(' ').map((v) => +v));
	}

	const up = arr.indexOf(-1);
	const down = up + C;
	for (let t = 0; t < T; t++) {
		const newArr = [];
		newArr.length = len;
		for (let i = 0; i < len; newArr[i++] = 0);
		/* ---------  확산  --------- */
		for (let cur = 0; cur < len; cur++) {
			if (arr[cur] <= 0) continue;
			let adj = [];
			let pos;
			const r = Math.floor(cur / C),
				c = cur % C;
			if (0 < r && arr[(pos = cur - C)] !== -1) adj.push(pos);
			if (r < R - 1 && arr[(pos = cur + C)] !== -1) adj.push(pos);
			if (0 < c && arr[(pos = cur - 1)] !== -1) adj.push(pos);
			if (c < C - 1) adj.push(cur + 1);
			const spread = Math.floor(arr[cur] / 5);
			for (const idx in adj) {
				newArr[adj[idx]] += spread;
			}
			newArr[cur] += arr[cur] - adj.length * spread;
		}
		/* ---------  순환  --------- */
		let upIdx, downIdx;
		for (upIdx = up - C; upIdx !== 0; upIdx -= C) {
			newArr[upIdx] = newArr[upIdx - C];
		}
		for (downIdx = down + C; downIdx !== len - C; downIdx += C) {
			newArr[downIdx] = newArr[downIdx + C];
		}
		for (let i = 0; i < C - 1; i++) {
			newArr[upIdx] = newArr[++upIdx];
			newArr[downIdx] = newArr[++downIdx];
		}
		for (; upIdx < up; upIdx += C) {
			newArr[upIdx] = newArr[upIdx + C];
		}
		for (; down + C < downIdx; downIdx -= C) {
			newArr[downIdx] = newArr[downIdx - C];
		}
		for (let i = 0; i < C - 2; i++) {
			newArr[upIdx] = newArr[--upIdx];
			newArr[downIdx] = newArr[--downIdx];
		}
		newArr[up + 1] = 0;
		newArr[down + 1] = 0;
		newArr[up] = -1;
		newArr[down] = -1;
		arr = newArr;
	}
	let ans = 0;
	for (const val of arr) ans += val;
	console.log(ans + 2);
}

solve();
