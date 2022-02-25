from sys import stdin
from heapq import heappush, heappop, heapify

input = stdin.readline


def solve():
    n, m = map(int, input().split())
    # edge[먼저 풀어야하는 문제] = [나중에 풀어야 하는 문제들]
    edge = [[] for _ in range(n+1)]
    # indegree[i]: i보다 선행되어 풀어야하는 문제들 중 푼 문제를 제외한 수
    indegree = [0] * (n + 1)
    ans = [0] * n
    for _ in range(m):
        before, after = map(int, input().split())
        edge[before].append(after)
        indegree[after] += 1

    idx = 0
    heap = [i for i in range(1, n+1) if indegree[i] == 0]
    heapify(heap)

    while heap:
        before = heappop(heap)
        ans[idx] = before
        idx += 1
        for after in edge[before]:
            indegree[after] -= 1
            if indegree[after] == 0:
                heappush(heap, after)

    return ans


if __name__ == '__main__':
    print(*solve())
