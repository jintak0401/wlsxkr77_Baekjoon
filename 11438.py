from sys import stdin, setrecursionlimit as SRL
from math import log2, ceil

input = stdin.readline
SRL(100_010)


def solve():
    N = int(input())
    connect = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        connect[a].append(b)
        connect[b].append(a)

    visited = [False] * (N + 1)
    depth = [0] * (N + 1)
    parent = [[0] for _ in range(N + 1)]
    max_depth = 0
    log_depth = 0

    def init(d, node):
        nonlocal max_depth
        visited[node] = True
        depth[node] = d
        if max_depth < d: max_depth = d
        for child in connect[node]:
            if visited[child]: continue
            parent[child][0] = node
            init(d+1, child)

    def set_parent():
        nonlocal log_depth
        log_depth = ceil(log2(max_depth))
        for i in range(N + 1):
            parent[i][1:] = [0] * log_depth

        for i in range(1, log_depth):
            for j in range(1, N + 1):
                parent[j][i] = parent[parent[j][i - 1]][i - 1]

    def query(a, b):
        if depth[a] > depth[b]:
            a, b = b, a

        tmp = 1 << log_depth
        for i in range(log_depth, -1, -1):
            if depth[b] - depth[a] >= tmp:
                b = parent[b][i]
            tmp //= 2

        if a == b:
            return b

        for i in range(log_depth, - 1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]

        return parent[a][0]

    init(0, 1)
    set_parent()

    for _ in range(int(input())):
        print(query(*map(int, input().split())))


if __name__ == '__main__':
    solve()

