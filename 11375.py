from sys import stdin, setrecursionlimit as SRL
SRL(10 ** 5)

input = stdin.readline


# 이분매칭
def bipartite_matching(vertex, here, connected_vertex, visited):
    for there in vertex[here]:
        if not visited[there]:
            visited[there] = True
            if (not connected_vertex[there]) or bipartite_matching(vertex, connected_vertex[there], connected_vertex, visited):
                connected_vertex[there] = here
                return True

    return False


def solve(n, m):
    worker = [0] * (n + 1)
    for i in range(1, n + 1):
        _, *worker[i] = [*map(int, input().split())]

    ans = 0
    connected_vertex = [0] * (m + 1)

    for i in range(1, len(worker)):
        visited = [False] * (m + 1)
        if bipartite_matching(worker, i, connected_vertex, visited):
            ans += 1

    return ans


if __name__ == '__main__':
    N, M = map(int, input().split())
    print(solve(N, M))
