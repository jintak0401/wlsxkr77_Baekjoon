const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const N = +input[inputIdx++];
	const N2 = N * N;
	const maxDepth = 5;
	let initBoard = [];
	for (let i = 0; i < N; i++)
		initBoard.push(...input[inputIdx++].split(' ').map((v) => +v));

	let already = new Set();

	const getIdx = (dir, ver, hor) => {
		// 상
		if (dir === 0) return ver + N * hor;
		// 하
		else if (dir === 1) return ver + N * (N - 1 - hor);
		// 좌
		else if (dir === 2) return hor * N + ver;
		// 우
		else return hor * N + (N - 1 - ver);
	};

	const dfs = (depth, board) => {
		if (depth === maxDepth) {
			return Math.max(...board);
		}
		already.add(board.join(','));
		let arr = [],
			val,
			ret = Math.max(...board),
			tmp = [],
			ableToSum,
			tmp2;
		arr.length = N2;
		tmp.length = N;
		for (let dir = 0; dir < 4; dir++) {
			arr.fill(0);
			for (let i = 0; i < N; i++) {
				for (let j = 0; j < N; j++)
					tmp[j] = board[getIdx(dir, ...(dir <= 1 ? [i, j] : [j, i]))];
				tmp2 = tmp.reduce((prev, cur) => {
					if (cur === 0) return prev;
					else if (prev.length && prev[prev.length - 1] === cur && ableToSum) {
						prev[prev.length - 1] += cur;
						ableToSum = false;
					} else {
						prev.push(cur);
						ableToSum = true;
					}
					return prev;
				}, []);
				for (let j = 0; j < tmp2.length; j++)
					arr[getIdx(dir, ...(dir <= 1 ? [i, j] : [j, i]))] = tmp2[j];
			}
			if (!already.has(arr.join(',')) && ret < (val = dfs(depth + 1, arr)))
				ret = val;
		}
		return ret;
	};

	return dfs(0, initBoard);
}

console.log(solve());
