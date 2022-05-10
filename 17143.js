const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const [R, C, M] = input[inputIdx++].split(' ').map((v) => +v);
	const len = R * C;

	// 상어우리 초기화
	let sharks = {};
	let pos;

	for (let i = 0; i < M; i++) {
		let [r, c, s, d, z] = input[inputIdx++].split(' ').map((v) => +v);
		pos = (r - 1) * C + (c - 1);
		s %= 2 * (d <= 2 ? R - 1 : C - 1);
		sharks[pos] = [s, d, z];
	}

	// 상어 이동
	const moveSharks = () => {
		let nxtSharks = {},
			nxtPos,
			nxtDir,
			v, x,
			l, mul, _2l;
		for (const pos in sharks) {
			// 이동
			[v, nxtDir] = sharks[pos];

			if (nxtDir <= 2) {
				nxtPos = pos % C;
				x = Math.floor(pos / C);
				l = R;
				mul = C;
			}
			else {
				nxtPos = Math.floor(pos / C) * C;
				x = pos % C;
				l = C;
				mul = 1;
			}
			_2l = 2 * l;

			if (nxtDir === 1 || nxtDir === 4){
				if (v <= x) nxtPos += mul * (x - v);
				else if (v <= x + l - 1) {
					nxtPos += mul * (v - x);
					nxtDir = nxtDir === 1 ? 2 : 3;
				}
				else nxtPos += mul * (_2l + x - 2 - v);
			}
			else {
				if (v <= l - 1 - x) nxtPos += mul * (x + v);
				else if (v <= _2l - 2 - x) {
					nxtPos += mul * (_2l - x - v - 2);
					nxtDir = nxtDir === 2 ? 1 : 4;
				}
				else nxtPos += mul * (v + x + 2 - _2l);
			}
			if (!nxtSharks[nxtPos] || nxtSharks[nxtPos][2] < sharks[pos][2]) {
				sharks[pos][1] = nxtDir;
				nxtSharks[nxtPos] = sharks[pos];
			}
		}
		return nxtSharks;
	};

	// 최상단 상어 잡기
	const getShark = (line) => {
		for (let i = line; i < len; i += C) {
			if (sharks[i]) return i;
		}
		return -1;
	};

	let ans = 0;
	for (let i = 0; i < C; i++) {
		if ((pos = getShark(i)) !== -1) {
			ans += sharks[pos][2];
			delete sharks[pos]
		}
		sharks = moveSharks();
	}
	return ans;
}

console.log(solve());
