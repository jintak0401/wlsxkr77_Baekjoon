from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def solve():
    N, P, K = map(int, input().split())
    connect = [[] for _ in range(N + 1)]
    inf = 1_000_001
    cand = set([0])
    for _ in range(P):
        a, b, c = map(int, input().split())
        connect[a].append((b, c))
        connect[b].append((a, c))
        cand.add(c)

    def dijkstra(val):
        # dist[i]: i번째에 인터넷을 연결할 때 val 보다 비용이 큰 갯수
        dist = [inf] * (N + 1)
        dist[1] = 0
        # (val 보다 비용이 큰 갯수, 몇 번째 컴퓨터)
        heap = [(0, 1)]
        while heap:
            cost, pos = heappop(heap)
            if dist[pos] < cost:
                continue
            for nxt, nxt_cost in connect[pos]:
                tmp = cost + 1 if nxt_cost > val else cost
                if tmp < dist[nxt]:
                    dist[nxt] = tmp
                    heappush(heap, (tmp, nxt))

        return dist[N] <= K

    if not dijkstra(inf): return -1

    cand = sorted(cand)
    lo, hi = 0, len(cand) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if dijkstra(cand[mid]):
            hi = mid - 1
        else:
            lo = mid + 1

    return cand[lo]


if __name__ == '__main__':
    print(solve())

