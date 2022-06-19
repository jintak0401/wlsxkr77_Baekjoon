const fs = require('fs');

const compare = (a, b) => {
	let val = 0;
	for (let i = 0; i < a.length; i++) {
		val = a[i] - b[i];
		if (val !== 0) return val;
	}
	return 0;
};

const heappush = (heap, element, cmp = compare) => {
	heap.push(element);
	let idx = heap.length - 1;
	let parentIdx = 0;
	const last = heap[idx];

	while (idx) {
		parentIdx = Math.floor((idx - 1) / 2);
		if (cmp(heap[parentIdx], last) > 0) {
			heap[idx] = heap[parentIdx];
			idx = parentIdx;
		} else break;
	}

	heap[idx] = last;
};

const heappop = (heap, cmp = compare) => {
	if (heap.length === 0) return undefined;

	const min = heap[0];
	const last = heap.pop();
	const len = heap.length;
	if (len !== 0) {
		let leftIdx,
			rightIdx,
			smallIdx,
			idx = 0;
		while ((leftIdx = 2 * idx + 1) < len) {
			rightIdx = leftIdx + 1;
			smallIdx =
				rightIdx < len && cmp(heap[rightIdx], heap[leftIdx]) <= 0
					? rightIdx
					: leftIdx;
			if (cmp(last, heap[smallIdx]) > 0) {
				heap[idx] = heap[smallIdx];
				idx = smallIdx;
			} else break;
		}
		heap[idx] = last;
	}
	return min;
};

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const N = +input[inputIdx++];
	const M = +input[inputIdx++];
	const dist = [];
	dist.length = N + 1;
	for (let i = 1; i <= N; dist[i++] = []);

	for (let i = 0; i < M; i++) {
		const [start, end, cost] = input[inputIdx++].split(' ').map((v) => +v);
		dist[start].push([end, cost]);
	}

	const [start, end] = input[inputIdx++].split(' ').map((v) => +v);
	const heap = [[0, start]];
	const visited = [];
	visited.length = N + 1;
	for (let i = 1; i <= N; visited[i++] = false);
	while (true) {
		const [curCost, curPos] = heappop(heap);
		if (curPos === end) return curCost;
		else if (visited[curPos]) continue;
		visited[curPos] = true;

		for (const [nxtPos, nxtCost] of dist[curPos]) {
			if (visited[nxtPos]) continue;
			heappush(heap, [curCost + nxtCost, nxtPos]);
		}
	}
}

console.log(solve());
