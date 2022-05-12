const fs = require('fs');

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const arr = [];
	arr.length = 10;
	for (let i = 0; i < 10; i++) {
		const line = input[inputIdx++];
		let num = '';
		for (const c of line) num += c === 'O' ? '1' : '0';
		arr[i] = parseInt(num, 2);
	}

	function hit(firstRow) {
		let needHit = firstRow;
		let cnt = 0;
		let middle = 0,
			up = 0;
		for (let i = 0; i < 10; i++) {
			cnt += (needHit.toString(2).match(/1/g) || []).length;
			[middle, up] = [up, needHit];
			needHit = middle ^ (up >> 1) ^ up ^ ((up << 1) & 1023) ^ arr[i];
		}
		return needHit === 0 ? cnt : 101;
	}

	let ans = 101;
	for (let i = 0; i < 1023; i++) {
		const val = hit(i);
		if (val < ans) ans = val;
	}
	return ans !== 101 ? ans : -1;
}

console.log(solve());
