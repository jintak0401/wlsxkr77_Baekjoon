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
	const N = +input[inputIdx++];
	const outDegree = [];
	const countNeed = [];
	const time = [];
	const ans = [];
	countNeed.length = N + 1;
	outDegree.length = N + 1;
	time.length = N + 1;
	ans.length = N + 1;
	for (let i = 1; i <= N; i++) {
		outDegree[i] = [];
	}
	for (let i = 1; i <= N; i++) {
		const [t, ...need] = input[inputIdx++].split(' ').map((v) => +v);
		time[i] = t;
		countNeed[i] = need.length - 1;
		for (const before of need.slice(0, -1)) {
			outDegree[before].push(i);
		}
	}

	const heap = [];
	for (let i = 1; i <= N; i++) {
		if (countNeed[i] === 0) heappush(heap, [time[i], i]);
	}

	while (heap.length) {
		const [t, cur] = heappop(heap);
		ans[cur] = t;
		for (const nxt of outDegree[cur]) {
			countNeed[nxt]--;
			if (countNeed[nxt] === 0) {
				heappush(heap, [t + time[nxt], nxt]);
			}
		}
	}

	for (let i = 1; i <= N; i++) {
		console.log(ans[i]);
	}
}

solve();
