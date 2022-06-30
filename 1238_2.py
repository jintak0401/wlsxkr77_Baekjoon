from sys import stdin

input = stdin.readline


def solve():
    N, M, X = map(int, input().split())
    inf = 1_000_000_000
    arr = [[inf] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        arr[a][b] = c

    for i in range(1, N + 1):
        arr[i][i] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            if arr[i][k] != inf:
                for j in range(1, N + 1):
                    if (tmp := arr[i][k] + arr[k][j]) < arr[i][j]:
                        arr[i][j] = tmp

    return max(arr[i][X] + arr[X][i] for i in range(1, N + 1))


if __name__ == '__main__':
    print(solve())
