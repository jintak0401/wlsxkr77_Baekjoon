const fs = require('fs');

const compare = (a, b) => {
	if (typeof a === 'number') return a - b;
	else {
		let val = 0;
		for (let i = 0; i < a.length; i++) {
			val = a[i] - b[i];
			if (val !== 0) return val;
		}
		return 0;
	}
};

const heappush = (heap, element) => {
	heap.push(element);
	let idx = heap.length - 1;
	let parentIdx = 0;
	const last = heap[idx];

	while (idx) {
		parentIdx = Math.floor((idx - 1) / 2);
		if (compare(heap[parentIdx], last) > 0) {
			heap[idx] = heap[parentIdx];
			idx = parentIdx;
		} else break;
	}

	heap[idx] = last;
};

const heappop = (heap) => {
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
				rightIdx < len && compare(heap[rightIdx], heap[leftIdx]) <= 0
					? rightIdx
					: leftIdx;
			if (compare(last, heap[smallIdx]) > 0) {
				heap[idx] = heap[smallIdx];
				idx = smallIdx;
			} else break;
		}
		heap[idx] = last;
	}
	return min;
};

const heapify = (heap) => {
	const len = heap.length;
	let leftIdx, rightIdx, smallIdx, rootIdx, tmp;

	const build = (idx) => {
		rootIdx = idx;
		leftIdx = 2 * idx + 1;
		rightIdx = leftIdx + 1;
		smallIdx =
			rightIdx < len && compare(heap[rightIdx], heap[leftIdx]) <= 0
				? rightIdx
				: leftIdx;

		if (compare(heap[rootIdx], heap[smallIdx]) > 0) {
			tmp = heap[rootIdx];
			heap[rootIdx] = heap[smallIdx];
			heap[smallIdx] = tmp;
			if (2 * smallIdx + 1 < len) build(smallIdx);
		}
	};

	for (let i = Math.floor(len / 2) - 1; i >= 0; i--) {
		build(i);
	}
};

function solve() {
	let input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;

	const T = +input[inputIdx++];
	for (let t = 0; t < T; t++) {
		const [N, K] = input[inputIdx++].split(' ').map((v) => +v);
		const time = [0, ...input[inputIdx++].split(' ').map((v) => +v)];
		const indegree = Array.from({ length: N + 1 }, () => 0);
		const outdegree = Array.from({ length: N + 1 }, () => []);
		for (let i = 0; i < K; i++) {
			const [before, after] = input[inputIdx++].split(' ').map((v) => +v);
			indegree[after] += 1;
			outdegree[before].push(after);
		}
		const W = +input[inputIdx++];
		const start = indegree.reduce((prev, cur, idx) => {
			if (idx !== 0 && cur === 0) prev.push(idx);
			return prev;
		}, []);
		const heap = start.map((idx) => [time[idx], idx]);
		heapify(heap);
		while (heap.length !== 0) {
			const [curTime, building] = heappop(heap);
			if (building === W) {
				console.log(curTime);
				break;
			}
			for (const nxt of outdegree[building]) {
				if (--indegree[nxt] === 0) {
					heappush(heap, [curTime + time[nxt], nxt]);
				}
			}
		}
	}
}

solve();
