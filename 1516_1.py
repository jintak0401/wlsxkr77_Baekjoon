from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def solve():
    N = int(input())
    time = [0] * (N + 1)
    out_degree = [[] for _ in range(N + 1)]
    need_count = [0] * (N + 1)
    for i in range(1, N + 1):
        t, *need, _ = map(int, input().split())
        time[i] = t
        for before in need:
            out_degree[before].append(i)
            need_count[i] += 1

    # (걸린 시간, 지은 건물)
    heap = [(time[i], i) for i in range(1, N + 1) if need_count[i] == 0]

    ans = [0] * (N + 1)

    while heap:
        t, cur = heappop(heap)
        ans[cur] = t

        for nxt in out_degree[cur]:
            need_count[nxt] -= 1
            if need_count[nxt] == 0:
                heappush(heap, (t + time[nxt], nxt))

    print(*ans[1:], sep="\n")


if __name__ == '__main__':
    solve()
