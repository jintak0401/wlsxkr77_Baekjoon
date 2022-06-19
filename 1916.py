from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def solve():
    N = int(input())
    M = int(input())
    dist = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end, cost = map(int, input().split())
        dist[start].append((end, cost))

    start, end = map(int, input().split())
    heap = [(0, start)]
    visited = [False] * (N + 1)
    while True:
        cur_cost, cur_pos = heappop(heap)
        if cur_pos == end: return cur_cost
        elif visited[cur_pos]: continue
        visited[cur_pos] = True

        for nxt_pos, nxt_cost in dist[cur_pos]:
            if visited[nxt_pos]: continue
            heappush(heap, (cur_cost + nxt_cost, nxt_pos))


if __name__ == '__main__':
    print(solve())
