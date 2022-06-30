const fs = require('fs');

const compare = (a, b) => {
	return a[0] - b[0];
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

function solve() {
	const input = fs.readFileSync('/dev/stdin').toString().split('\n');
	let inputIdx = 0;
	const inf = 1_000_000_000;

	const [N, M, X] = input[inputIdx++].split(' ').map((v) => +v);

	let go = [],
		back = [];
	go.length = N + 1;
	back.length = N + 1;
	for (let i = 1; i <= N; i++) {
		go[i] = [];
		back[i] = [];
	}
	for (let i = 0; i < M; i++) {
		const [from, to, dist] = input[inputIdx++].split(' ').map((v) => +v);
		go[from].push([to, dist]);
		back[to].push([from, dist]);
	}

	const dijkstra = (graph) => {
		let tmp;
		const cost = [];
		cost.length = N + 1;
		for (let i = 1; i <= N; cost[i++] = inf);
		cost[X] = 0;
		const heap = [[0, X]];
		while (heap.length) {
			const [curCost, curPos] = heappop(heap);
			if (cost[curPos] < curCost) continue;
			for (const [nxtPos, nxtCost] of graph[curPos]) {
				if ((tmp = curCost + nxtCost) < cost[nxtPos]) {
					cost[nxtPos] = tmp;
					heappush(heap, [tmp, nxtPos]);
				}
			}
		}
		return cost;
	};

	let max = -1;
	go = dijkstra(go);
	back = dijkstra(back);
	for (let i = 1; i <= N; i++) {
		let tmp = go[i] + back[i];
		if (max < tmp) max = tmp;
	}

	return max;
}

console.log(solve());
