from sys import stdin
from collections import deque


input = stdin.readline


def solve():
    N, M = map(int, input().split())
    # edge[앞에 서야 하는 학생] = [뒤에 서야하는 학생]
    edge = [[] for _ in range(N + 1)]
    # indegree[i] = i학생보다 먼저 서야하는 학생들 중 아직 서지 않은 학생 수
    indegree = [0] * (N + 1)
    for i in range(M):
        before, after = map(int, input().split())
        edge[before].append(after)
        indegree[after] += 1

    ans = [0] * N
    idx = 0
    q = deque([i for i in range(1, N + 1) if indegree[i] == 0])

    while q:
        before = q.popleft()
        ans[idx] = before
        idx += 1

        for after in edge[before]:
            indegree[after] -= 1
            if indegree[after] == 0:
                q.append(after)

    return ans


if __name__ == '__main__':
    print(*solve())
