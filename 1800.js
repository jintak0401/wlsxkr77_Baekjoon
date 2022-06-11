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

	const inf = 1_000_001;
	const [N, P, K] = input[inputIdx++].split(' ').map((v) => +v);
	let cand = new Set([0]);
	const connect = [];
	connect.length = N + 1;
	for (let i = 1; i <= N; connect[i++] = []);
	for (let i = 0; i < P; i++) {
		const [a, b, c] = input[inputIdx++].split(' ').map((v) => +v);
		connect[a].push([b, c]);
		connect[b].push([a, c]);
		cand.add(c);
	}

	const dijkstra = (val) => {
		const dist = [];
		dist.length = N + 1;
		dist[1] = 0;
		for (let i = 2; i <= N; dist[i++] = inf);

		const heap = [[0, 1]];

		let tmp;
		while (heap.length) {
			const [cost, pos] = heappop(heap);
			if (dist[pos] < cost) continue;
			for (const [nxt, nxtCost] of connect[pos]) {
				if (nxtCost > val && (tmp = cost + 1) < dist[nxt]) {
					dist[nxt] = tmp;
					heappush(heap, [tmp, nxt]);
				} else if (nxtCost <= val && cost < dist[nxt]) {
					dist[nxt] = cost;
					heappush(heap, [cost, nxt]);
				}
			}
		}
		return dist[N] <= K;
	};

	if (!dijkstra(inf)) return -1;

	cand = [...cand].sort((a, b) => a - b);
	let lo = 0,
		hi = cand.length - 1;

	while (lo <= hi) {
		const mid = Math.floor((lo + hi) / 2);
		dijkstra(cand[mid]) ? (hi = mid - 1) : (lo = mid + 1);
	}

	return cand[lo];
}

console.log(solve());
