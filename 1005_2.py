from sys import stdin
from heapq import heapify, heappush, heappop

input = stdin.readline


def solve():
    N, K = map(int, input().split())
    time = [0, *map(int, input().split())]
    outdegree = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for _ in range(K):
        before, after = map(int, input().split())
        outdegree[before].append(after)
        indegree[after] += 1

    W = int(input())
    if indegree[W] == 0:
        return time[W]
    heap = [[time[i], i] for i in range(1, N + 1) if indegree[i] == 0]
    heapify(heap)

    while heap:
        t, cur = heappop(heap)
        for nxt in outdegree[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                if nxt == W:
                    return t + time[nxt]
                heappush(heap, [t + time[nxt], nxt])


if __name__ == '__main__':
    for _ in range(int(input())):
        print(solve())
